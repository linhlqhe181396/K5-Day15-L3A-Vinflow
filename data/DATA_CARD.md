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
| Dùng để làm gì | Nguồn 7 câu khiếu nại tiếng Anh giả lập cho `eval/benchmark.csv` (ghi `sinh_seed`, gồm `missing_item`, `late_delivery`, `wrong_order`, `payment_issue`) và tham khảo phân loại ý định cho lát cắt Track D |
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
| Dùng để làm gì | Bằng chứng pain thực tế từ người trả lời (`evidence/summary.md`), căn cứ đặt `why` cho `eval/metric_spec.yaml`, và nguồn tạo 10 ca diễn đạt lại từ phiếu khảo sát trong `eval/benchmark.csv` (B21–B30) |
| Từ đâu | [Google Forms do nhóm cung cấp](https://docs.google.com/forms/d/e/1FAIpQLSfJh11wzUJBxc-Z6II5ogO9SCjTjpNJI6JBGqDz-x1VH9yrAA/viewform?usp=publish-editor), xuất CSV 30 phản hồi. Theo nhóm, gửi cho người dùng app đặt đồ ăn, chủ yếu bạn bè/người quen đồng lứa; nhóm xác nhận 30/30 phiếu ngoài nhóm. CSV ẩn danh không tự kiểm được danh tính/kênh phát. |
| Xử lý những bước gì | Không thu thập họ tên, email, SĐT; giữ nguyên 30 dòng; thống kê tỷ lệ phân bố từng câu hỏi. Script `evidence/derive_survey_cases.py` chuyển lựa chọn của 10 phiếu thành câu ngôi thứ nhất, giữ các khả năng “hoặc” trong đáp án gốc, không thêm mã đơn/món/tiền và ghi rõ số dòng nguồn. Đây là diễn đạt lại, không phải lời kể nguyên văn. |
| Số dòng / số đoạn | 30 phản hồi (30/30 từng đặt đồ ăn trong 1 tháng qua và từng gặp thiếu món/giao trễ; 11/30 gặp cả hai; 24/30 không gửi khiếu nại hoặc thấy xử lý chậm/rườm rà) |
| Phiên bản / ngày lấy | Thu thập ngày 27/11/2026 (18:05–18:19) |
| Nhãn | `thật` (phản hồi người dùng thật) |
| Giới hạn | Cỡ mẫu `n = 30`, câu hỏi dạng lựa chọn (không có câu trả lời mở nguyên văn) và thu thập trong 1 ngày; 30/30 ngoài nhóm là xác nhận của nhóm, không kiểm độc lập được từ CSV ẩn danh. Kênh phát cụ thể chưa ghi. Các câu diễn đạt lại chỉ bảo toàn nội dung phương án đã chọn. |

## Dataset 3 · Đơn hàng và chính sách giả lập cho bản chạy thử

`data/orders.json` chứa 3 đơn giả (`VF-1042`, `VF-2088`, `VF-1001`) với tên món, giá món, tổng đơn, số phút giao trễ và số khiếu nại trong 30 ngày. `data/policy.md` ghi CS-01…CS-04, mọi hạn mức đều *(tự ước tính)*. Hai file chỉ dùng để chạy công cụ tra đơn và kiểm hạn mức trong bản CP2; không phải đơn hoặc chính sách của app thật. `VF-9999` cố ý không có để thử nhánh chuyển người.

**Nguồn bộ câu thử hiện tại:** 13/30 câu `tu_viet` do nhóm tự viết (3 câu lấy ý tưởng từ khảo sát), 7/30 câu `sinh_seed` từ dataset giả lập, 10/30 câu `data_that` là **diễn đạt lại có truy vết đến từng dòng khảo sát thật**. Lượt `run-1` đã chấm trên 20 câu B01–B20 trước khi thêm B21–B30; không sửa lượt này. Data tự dựng **không phải bằng chứng pain**.
