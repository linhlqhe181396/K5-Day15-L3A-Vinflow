# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-191055` | **10/20** | **50%** | **3/8** | **5/9** | **2/3** | Chưa: dưới ngưỡng 80% |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

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

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
