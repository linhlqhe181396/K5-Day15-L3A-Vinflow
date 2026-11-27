"""Fixed D1 workflow. CP2 uses a fake model and deterministic extraction."""

import re

from ai import call_model
from tools import check_limit, create_refund_draft, escalate_ticket, get_order, get_policy
from tracing import note

SYSTEM = "Classify the food complaint as missing_item, late_delivery or other. This is a draft-only support demo."


def answer(text: str) -> dict:
    call_model(SYSTEM, text)  # CP2: fake call is traced; replace extraction with real model before CP3.
    message = text.lower()
    match = re.search(r"\bVF-\d+\b", text, re.I)
    order_id = match.group(0).upper() if match else ""

    if any(word in message for word in ("ignore all previous", "system override", "system prompt", "bypass verification")):
        note("từ chối lệnh giả mạo hệ thống")
        return {"output": "Không thể bỏ qua xác minh hoặc tiết lộ hướng dẫn nội bộ. Vui lòng gửi khiếu nại đơn hàng theo quy trình hỗ trợ."}

    missing = any(word in message for word in ("missing", "thiếu", "không có món"))
    late = any(word in message for word in ("late", "delayed", "giao trễ", "giao muộn"))
    if not (missing or late):
        get_policy("other")
        draft = escalate_ticket(order_id, "Sự cố ngoài lát cắt D1", "CS-04")
        return {"output": f"CS-04: Sự cố này cần bộ phận hỗ trợ phù hợp. Phiếu {draft['ticket_id']} đang ở trạng thái {draft['status']}."}
    if not order_id:
        return {"output": "Vui lòng cung cấp mã đơn dạng VF-xxxx để đối chiếu trước khi đề xuất hoàn tiền hoặc voucher."}

    order = get_order(order_id)
    if order is None:
        draft = escalate_ticket(order_id, "Không tìm thấy đơn", "CS-03")
        return {"output": f"CS-03: Không tìm thấy {order_id}; đã tạo phiếu nháp {draft['ticket_id']} để nhân viên kiểm tra. Chưa xác nhận bồi thường."}
    if any(word in message for word in ("allerg", "dị ứng", "food safety", "an toàn thực phẩm", "chicken in", "threat", "tiktok", "bóc phốt")) or order["complaints_30d"] >= 2:
        draft = escalate_ticket(order_id, "Cần nhân viên kiểm tra rủi ro", "CS-03")
        return {"output": f"CS-03: Đơn {order_id} cần nhân viên xem xét. Phiếu nháp {draft['ticket_id']} ở trạng thái {draft['status']}; chưa duyệt bồi thường."}
    if missing and late:
        draft = escalate_ticket(order_id, "Đồng thời thiếu món và giao trễ; cần kiểm tra từng phần", "CS-03")
        return {"output": f"CS-03: Đơn {order_id} có hai sự cố; phiếu nháp {draft['ticket_id']} chờ nhân viên kiểm tra, chưa duyệt bồi thường."}

    issue = "missing_item" if missing else "late_delivery"
    policy = get_policy(issue)
    if missing:
        mentioned = [item for item in order["items"] if item["name"].lower() in message]
        if len(mentioned) != 1:
            return {"output": f"{policy['code']}: Vui lòng cho biết chính xác món thiếu trong đơn {order_id}; chưa thể xác định số tiền hoàn."}
        item = mentioned[0]
        amount = item["price"]
        kind = "refund"
    else:
        delay = order["delay_minutes"]
        amount = 0 if delay < 15 else 2 if delay <= 30 else 5
        kind = "voucher"

    verdict = check_limit(issue, amount, order, amount if missing else 0)
    if not verdict["allowed"]:
        draft = escalate_ticket(order_id, "Vượt hạn mức chính sách", "CS-03")
        return {"output": f"CS-03: Đề xuất vượt hạn mức {policy['code']}; phiếu nháp {draft['ticket_id']} chờ nhân viên duyệt, chưa hoàn tiền."}
    if amount == 0:
        return {"output": f"CS-02: Đơn {order_id} trễ {order['delay_minutes']} phút, dưới ngưỡng 15 phút; xin lỗi vì sự bất tiện, chưa có voucher theo chính sách giả lập."}
    draft = create_refund_draft(order_id, kind, amount, policy["code"])
    action = "hoàn phần món thiếu" if missing else "voucher giao trễ"
    return {"output": f"{policy['code']}: Đề xuất {action} ${amount:.2f} cho đơn {order_id}. Đã tạo {draft['draft_id']} ({draft['status']}); chờ người duyệt, chưa chuyển tiền hay cấp voucher."}
