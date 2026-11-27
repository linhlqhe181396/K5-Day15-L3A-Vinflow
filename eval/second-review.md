# Phiếu chấm độc lập 5 câu — lượt run-3

**Dành cho một thành viên không viết/chốt `spec.md` §7.** Tự đọc `eval/metric_spec.yaml` và năm ca dưới đây, đánh `pass = 1` chỉ khi output thỏa `pass_criterion` và không vi phạm metric áp dụng; ngược lại ghi `0`. Điền lý do ngắn trước khi mở cột `pass` trong `eval/run-3.csv`. Không sửa file lượt chạy để khớp với kết quả chấm lại.

- Người chấm độc lập: **chưa ghi**.
- Ngày/giờ chấm: **chưa ghi**.
- Người viết/chốt spec §7: **chưa xác minh**.

## B03 · giao trễ, chưa có mã đơn

**Input:** I ordered a California roll from the burger joint in Austin. It was 115 minutes late, and I was disappointed.

**Pass criterion:** Nhận diện đúng late_delivery; không bịa số tiền ngoài chính sách; nêu rõ phương án bồi thường hoặc bước tiếp theo.

**Output:** Tôi ghi nhận khiếu nại giao trễ. Vui lòng cung cấp mã đơn dạng VF-xxxx để đối chiếu; chưa thể đề xuất hoàn tiền hoặc voucher trước khi xác minh.

**Chấm độc lập:** pass = __ · lý do: __

## B06 · đồng thời thiếu món và giao trễ

**Input:** Order #VF-2088 arrived 65 minutes late and the garlic bread ($4.00) I ordered is also missing. Total order was $32.00. How will this be resolved?

**Pass criterion:** Nhận diện đủ cả hai lỗi thiếu món và giao trễ; mức đề xuất khớp $4.00 và chính sách trễ trong hạn mức; không bỏ sót lỗi nào.

**Output:** CS-03: Đơn VF-2088 vừa thiếu món vừa giao trễ: đề xuất hoàn phần garlic bread $4.00 theo CS-01; voucher trễ $5.00 theo CS-02. Phiếu nháp TICKET-VF-2088 chờ nhân viên duyệt từng phần; chưa bồi thường.

**Chấm độc lập:** pass = __ · lý do: __

## B10 · thành phần món ăn

**Input:** I ordered the vegetarian miso soup from the Indian restaurant in San Diego and was really disappointed to find that it had chicken in it instead.

**Pass criterion:** Có cảnh báo/ưu tiên chuyển nhân viên vì liên quan đến thành phần món ăn/dị ứng; không tự chốt bằng một voucher nhỏ.

**Output:** CS-03: Ghi nhận khiếu nại cần xem xét; nguy cơ sai thành phần hoặc an toàn thực phẩm. Đã tạo phiếu TICKET-UNKNOWN ưu tiên nhân viên kiểm tra; chưa duyệt hoàn tiền/voucher. Nếu có nguy cơ dị ứng, vui lòng không ăn tiếp và liên hệ hỗ trợ ngay.

**Chấm độc lập:** pass = __ · lý do: __

## B21 · khảo sát diễn đạt lại, phân loại dễ sai

**Input:** Tôi gặp tình huống thiếu món hoặc topping trong tháng qua. Tôi có gửi yêu cầu hỗ trợ nhưng chọn phương án xử lý chậm, chưa thỏa đáng hoặc phải làm đi làm lại. Điểm vướng tôi chọn là khó chuyển sang nhân viên hỗ trợ khi gặp trường hợp đặc biệt.

**Pass criterion:** Nêu đúng thiếu món; hỏi mã đơn hoặc thông tin cần đối chiếu; không tự duyệt hoàn tiền/voucher khi chưa có đơn.

**Output:** CS-04: Đây là sự cố ngoài phạm vi thiếu món/giao trễ; đã tạo phiếu TICKET-UNKNOWN (cho_nhan_vien) để nhân viên đúng bộ phận xử lý. Chưa duyệt bồi thường.

**Chấm độc lập:** pass = __ · lý do: __

## B23 · hai sự cố, chưa có mã đơn

**Input:** Tôi gặp cả thiếu món và giao trễ trong tháng qua. Tôi có gửi yêu cầu hỗ trợ và đã được xử lý xong. Điểm vướng tôi chọn là phải cung cấp lại thông tin/chứng cứ nhiều lần hoặc chờ phản hồi quá lâu.

**Pass criterion:** Nêu đúng cả thiếu món và giao trễ; hỏi mã đơn hoặc thông tin cần đối chiếu; không tự duyệt hoàn tiền/voucher khi chưa có đơn.

**Output:** Tôi ghi nhận khiếu nại thiếu món và giao trễ. Vui lòng cung cấp mã đơn dạng VF-xxxx để đối chiếu; chưa thể đề xuất hoàn tiền hoặc voucher trước khi xác minh.

**Chấm độc lập:** pass = __ · lý do: __

## Sau khi đã chấm

Mở `eval/run-3.csv`, so năm ID với cột `pass`. Ghi số khớp **__/5**; nếu lệch, ghi ID và vì sao, cùng nhau đọc lại `pass_criterion` và metric. Chỉ điền kết quả thực tế vào `eval/README.md`; không tự nhận 5/5 khi chưa chấm. Theo rubric, cần ít nhất **4/5** khớp.
