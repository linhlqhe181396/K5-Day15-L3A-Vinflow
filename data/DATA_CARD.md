# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Food Delivery Support Tickets

File CSV để dùng trong repo: `data/raw/food-delivery-support-tickets.csv` (chuyển từ file Parquet gốc, giữ nguyên 10.153 dòng và 10 cột). File Parquet gốc: `data/raw/food-delivery-support-tickets.parquet`.
Nguồn: https://huggingface.co/datasets/OrSabbach/food-delivery-support-tickets · giấy phép MIT theo dataset card · tải ngày 27/11/2026.
10.153 dòng hội thoại tiếng Anh do mô hình tạo, không phải khiếu nại thực tế. Dùng `customer_message` và `category` để tham khảo/huấn luyện nhận diện loại khiếu nại D1; trong đó `missing_item` 1.309 dòng, `late_delivery` 1.309 dòng, `wrong_order` 1.296 dòng, `cold_food` 1.297 dòng, `payment_issue` 1.265 dòng, `refund_request` 1.248 dòng, `courier_problem` 1.220 dòng, `cancellation` 1.209 dòng.
Không dùng `sentiment` và `urgency` làm nhãn chuẩn vì tác giả công bố chúng không đáng tin. Không dùng `resolution` hoặc `agent_reply` làm quyết định hoàn tiền chuẩn vì thiếu chi tiết món, bằng chứng và chính sách hạn mức. Dữ liệu này không chứng minh mức độ phổ biến của pain ngoài đời. Khi tạo bộ đánh giá tiếng Việt, tách khỏi tập dùng để huấn luyện.

| | |
|---|---|
| Dùng để làm gì | Nguồn câu khiếu nại tiếng Anh cho bộ câu thử `eval/benchmark.csv` (7/15 câu từ `data_that`, gồm `missing_item`, `late_delivery`, `wrong_order`, `payment_issue`) và tham khảo phân loại ý định cho lát cắt Track D |
| Từ đâu | Bộ dữ liệu công khai Hugging Face (`OrSabbach/food-delivery-support-tickets`, giấy phép MIT) do nhóm tải về và lưu tại `data/raw/food-delivery-support-tickets.csv` |
| Xử lý những bước gì | Chuyển từ Parquet sang CSV (UTF-8), kiểm tra phân bố 8 `category` (10.153 dòng, 10 cột), chọn lọc mẫu đại diện cho từng nhóm `thuong`/`kho` đưa vào `eval/benchmark.csv` |
| Số dòng / số đoạn | 10.153 dòng tổng cộng (trong đó 1.309 `missing_item`, 1.309 `late_delivery`); trích 7 mẫu vào `eval/benchmark.csv` |
| Phiên bản / ngày lấy | Tải ngày 27/11/2026 |
| Nhãn | `synthetic` (hội thoại tiếng Anh do mô hình tạo theo dataset card) |
| Giới hạn | Dữ liệu tiếng Anh, giả lập nên không dùng để chứng minh tần suất pain thực tế; `sentiment`/`urgency` thiếu tin cậy; `resolution`/`agent_reply` thiếu chi tiết món, bằng chứng ảnh và hạn mức hoàn tiền nên nhóm tự thiết kế tiêu chí chuẩn trong `eval/benchmark.csv` |

## Dataset 2 · Khảo sát người dùng đặt đồ ăn qua ứng dụng

File CSV để dùng trong repo: `data/raw/survey.csv` (30 dòng, 8 cột — gồm dấu thời gian và 7 câu hỏi trắc nghiệm).

| | |
|---|---|
| Dùng để làm gì | Bằng chứng pain thực tế từ người dùng (`evidence/summary.md`), căn cứ đặt `why` cho `eval/metric_spec.yaml`, và nguồn thiết kế kịch bản thực tế trong `eval/benchmark.csv` (ca gặp cả thiếu món và giao trễ — 36,7%; ca mức hoàn chưa khớp/chưa rõ lý do — 36,7%) |
| Từ đâu | Khảo sát trực tuyến (Google Forms) do nhóm tự thu thập từ người đặt đồ ăn qua app (ShopeeFood, GrabFood, BeFood, Xanh SM Ngon…) |
| Xử lý những bước gì | Không thu thập họ tên, email, SĐT; giữ nguyên 30 dòng hợp lệ; thống kê tỷ lệ phân bố từng câu hỏi để đưa vào `evidence/summary.md` và đối chiếu thiết kế câu thử |
| Số dòng / số đoạn | 30 phản hồi (30/30 từng đặt đồ ăn trong 1 tháng qua và từng gặp thiếu món/giao trễ; 11/30 gặp cả hai; 24/30 không gửi khiếu nại hoặc thấy xử lý chậm/rườm rà) |
| Phiên bản / ngày lấy | Thu thập ngày 27/11/2026 (18:05–18:19) |
| Nhãn | `thật` (phản hồi người dùng thật) |
| Giới hạn | Cỡ mẫu `n = 30`, câu hỏi dạng lựa chọn (không có câu trả lời mở nguyên văn) và thu thập trong 1 ngày; không đủ chi tiết từng mã đơn nên kết hợp với `food-delivery-support-tickets.csv` để tạo đầu vào tiếng Anh cho `eval/benchmark.csv` |

**Data `synthetic` (nhóm tự sinh):** Các câu `tu_viet` (5/15 câu trong `eval/benchmark.csv`) do nhóm tự viết bằng tiếng Anh để phủ đủ các ca vượt hạn mức (lớp 1/3), đe doạ leo thang (lớp 4), ngoài phạm vi và 2 câu tấn công (`tu_choi`). Data tự dựng **không phải bằng chứng pain**.
