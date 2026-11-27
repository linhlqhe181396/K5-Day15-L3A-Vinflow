# Báo cáo đánh giá — lượt 1, bộ mở rộng lượt 2, cải tiến lượt 3

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-N.csv` sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-191055` | **10/20** | **50%** | **3/8** | **5/9** | **2/3** | Chưa: dưới ngưỡng 80% |
| 2 | `run-2@20261127-192424` | **9/30** | **30%** | **3/15** | **4/12** | **2/3** | Chưa: dưới ngưỡng 80%; 6 câu lỗi API |
| 3 | `run-3@20261127-205753` | **26/30** | **87%** | **12/15** | **11/12** | **3/3** | Đạt chuẩn tổng ≥80%; 2 câu lỗi API |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`, `eval/run-3.csv`. Trace tương ứng trong `traces/`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Hỏi mã đơn nhưng không nói rõ loại sự cố | 4 | B01–B04 |
| Chuyển kênh chung, thiếu lý do hoặc phạm vi | 4 | B10, B11, B12, B13 |
| Thiếu phương án cho hai sự cố / thiếu bước tiếp theo | 2 | B06, B17 |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B03 | Giao trễ 115 phút, không có mã đơn | Chỉ hỏi mã đơn | Không nêu đây là giao trễ, dù không bịa voucher |
| B06 | `VF-2088` vừa trễ vừa thiếu bánh mì tỏi $4 | Chuyển nhân viên, không nêu mức nào | Không đáp ứng tiêu chí xử lý cả hai thiệt hại |
| B10 | Món chay có thịt gà | Chuyển kênh chung CS-04 | Không nêu nguy cơ thành phần/an toàn thực phẩm hoặc ưu tiên |

Lượt 1 chạy bằng Gemini thật, 20/20 câu không có lỗi API. Chấm từng câu trong `eval/run-1.csv` chỉ qua cột `pass` và `ghi_chu`; điểm được tính bằng `python run.py score eval/run-1.csv`. **Không sửa output, expected hay xóa câu trượt.**

## Lượt 2 — bộ 30 câu mở rộng

Kết quả `python run.py score eval/run-2.csv`: **9/30 (30%)**. Sáu câu lỗi kỹ thuật được chấm không đạt: B09 timeout, B22 HTTP 503, B26/B27/B29/B30 HTTP 429. Trong 24 câu có output, 9 câu đạt. Lỗi gốc giữ nguyên ở cột `error` và `traces/run-2.jsonl`.

Trong các câu có output, lỗi lặp lại là chỉ hỏi mã đơn mà chưa nhận diện thiếu món/giao trễ (B01–B04, B23, B24, B28), hoặc chuyển hỗ trợ chung mà không nêu đúng sự cố/lý do (B10, B12, B13, B21, B25). Lượt 1 có 20 câu, lượt 2 có 30 câu; hai tỷ lệ không thể dùng làm so sánh cải tiến trên cùng bộ thử. Chưa có thay đổi logic giữa hai lượt.

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: hỏi mã đơn nhưng không nêu loại sự cố, và chuyển nhân viên chung chung. Khảo sát ghi 11/30 người chọn vướng việc phải cung cấp lại thông tin hoặc chờ lâu; phản hồi không rõ làm tăng vòng hỏi lại.
- Đã sửa `codebase/agent.py` sau `run-2`: nêu thiếu món/giao trễ khi hỏi mã; ghi lý do chuyển kênh; đưa ca sai thành phần/đe dọa lên nhánh ưu tiên; nêu bước tiếp theo với đơn trễ dưới ngưỡng. Kiểm tra cục bộ bằng chế độ fake cho 5 tình huống, không dùng làm kết quả đánh giá AI thật.
- Kết quả sau sửa: `run-2` **9/30 (30%)** → `run-3` **26/30 (87%)** trên cùng bộ 30 câu, cùng tiêu chí chấm. Nhóm lỗi hỏi mã đơn không nêu loại sự cố B01–B04, B23, B24, B28: **0/7 → 7/7**. Hai lỗi API của `run-3` vẫn tính không đạt.
- Câu nào tệ đi sau khi sửa: không thấy câu có output trước đó đạt rồi trở thành câu có output trượt; B17 và B20 trượt do lỗi API trong `run-3`. Cần theo dõi ổn định qua nhiều lượt.

## 4. Còn lại

- Lỗi chưa sửa: B21–B22 bị phân loại nhầm thiếu món thành ngoài phạm vi; B17 HTTP 503, B20 timeout. `cost/simulate-1.csv` đã ghi 50 phiên, trong đó 36 phiên không lỗi và 14 phiên lỗi; xem giả định và kết quả tại `cost/cost-estimate.md`.
- Nếu có thêm 1 tuần: giảm lỗi phân loại B21–B22, thử với người dùng thật có đồng ý; đo chi phí và tỷ lệ lỗi API qua nhiều lượt. Trước khi nộp, một thành viên không viết chuẩn §7 cần chấm độc lập 5 output theo `eval/second-review.md`.

## Lượt 3 — sau thay đổi logic

`run-3` cùng bộ 30 câu với `run-2`, đạt **26/30 (87%)**. B21–B22 có output nhưng sai loại sự cố; B17 lỗi HTTP 503, B20 timeout nên tính không đạt. Theo `spec.md` §7, chuẩn tổng ≥80% đã qua; các ca nhạy cảm không tạo bản nháp tiền trái phép hoặc lộ prompt. Kết quả này chưa chứng minh hệ thống hết lỗi API hoặc đạt chuẩn cho mọi dữ liệu ngoài benchmark.
