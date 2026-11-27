"""Append ten labeled paraphrases of selected survey rows to the D1 benchmark.

Each input uses only answers selected on one survey row. These are not verbatim
free-text statements from a respondent. The original CSV is left untouched.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURVEY = ROOT / "data/raw/survey.csv"
BENCHMARK = ROOT / "eval/benchmark.csv"
LINES = [2, 3, 5, 6, 7, 9, 10, 16, 21, 26]

ISSUE = {
    "thiếu món / topping": ("Tôi gặp tình huống thiếu món hoặc topping trong tháng qua.", "thiếu món"),
    "giao trễ": ("Tôi gặp tình huống giao trễ trong tháng qua.", "giao trễ"),
    "gặp cả thiếu món và giao trễ": ("Tôi gặp cả thiếu món và giao trễ trong tháng qua.", "cả thiếu món và giao trễ"),
}
COMPLAINT = {
    "Có, nhưng xử lý chậm / chưa thỏa đáng / phải làm đi làm lại": "Tôi có gửi yêu cầu hỗ trợ nhưng chọn phương án xử lý chậm, chưa thỏa đáng hoặc phải làm đi làm lại.",
    "Có, và đã được xử lý xong": "Tôi có gửi yêu cầu hỗ trợ và đã được xử lý xong.",
    "Không gửi vì thấy thao tác rườm rà / mất thời gian / không kỳ vọng được giải quyết nhanh": "Tôi không gửi khiếu nại vì thấy thao tác rườm rà, mất thời gian hoặc không kỳ vọng được giải quyết nhanh.",
}
PAIN = {
    "Khó chuyển sang nhân viên hỗ trợ khi gặp trường hợp đặc biệt": "Điểm vướng tôi chọn là khó chuyển sang nhân viên hỗ trợ khi gặp trường hợp đặc biệt.",
    "Phải cung cấp lại thông tin/chứng cứ nhiều lần hoặc chờ phản hồi quá lâu": "Điểm vướng tôi chọn là phải cung cấp lại thông tin/chứng cứ nhiều lần hoặc chờ phản hồi quá lâu.",
    "Bot/hệ thống trả lời theo menu có sẵn, không hiểu đúng tình huống của mình": "Điểm vướng tôi chọn là bot theo menu có sẵn không hiểu đúng tình huống của mình.",
    "Mức hoàn tiền/voucher đưa ra chưa khớp thiệt hại thực tế hoặc không rõ lý do": "Điểm vướng tôi chọn là mức hoàn tiền/voucher chưa khớp thiệt hại hoặc không rõ lý do.",
}


def main():
    with SURVEY.open(encoding="utf-8-sig", newline="") as file:
        survey = list(csv.reader(file))
    with BENCHMARK.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        tests = list(reader)
    if any(test["id"] == "B21" for test in tests):
        raise SystemExit("B21–B30 đã có; không thêm lần nữa")
    if len(tests) != 20 or tests[-1]["id"] != "B20":
        raise SystemExit("Bộ câu thử nền đã đổi; kiểm tra trước khi thêm")

    for number, line in enumerate(LINES, start=21):
        row = survey[line - 1]
        opener, issue = ISSUE[row[2]]
        input_text = " ".join((opener, COMPLAINT[row[4]], PAIN[row[6]]))
        tests.append({
            "id": f"B{number}", "input": input_text,
            "expected": f"Ghi nhận đúng {issue}; hỏi mã đơn và thông tin còn thiếu trước khi quyết định tiền; phản hồi về bước hỗ trợ tiếp theo.",
            "pass_criterion": f"Nêu đúng {issue}; hỏi mã đơn hoặc thông tin cần đối chiếu; không tự duyệt hoàn tiền/voucher khi chưa có đơn.",
            "type": "kho" if issue == "cả thiếu món và giao trễ" else "thuong",
            "source": f"data_that: data/raw/survey.csv#dong-{line} (diễn đạt lại từ lựa chọn, không phải lời nguyên văn)",
        })
    with BENCHMARK.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(tests)
    print(f"Added {len(LINES)} survey-derived cases; total {len(tests)}")


if __name__ == "__main__":
    main()
