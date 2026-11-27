# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Food Delivery Support Tickets

File gốc cục bộ: `data/raw/food-delivery-support-tickets.parquet`.
Nguồn: https://huggingface.co/datasets/OrSabbach/food-delivery-support-tickets · giấy phép MIT theo dataset card · tải ngày 27/11/2026.
10.153 dòng hội thoại tiếng Anh do mô hình tạo, không phải khiếu nại thực tế. Dùng `customer_message` và `category` để tham khảo/huấn luyện nhận diện loại khiếu nại D1; trong đó `missing_item` 1.309 dòng, `late_delivery` 1.309 dòng, `wrong_order` 1.296 dòng.
Không dùng `sentiment` và `urgency` làm nhãn chuẩn vì tác giả công bố chúng không đáng tin. Không dùng `resolution` hoặc `agent_reply` làm quyết định hoàn tiền chuẩn vì thiếu chi tiết món, bằng chứng và chính sách hạn mức. Dữ liệu này không chứng minh mức độ phổ biến của pain ngoài đời. Khi tạo bộ đánh giá tiếng Việt, tách khỏi tập dùng để huấn luyện.

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ `…` · bộ câu thử · đào bằng chứng |
| Từ đâu | data BTC cấp (`…` trong repo đề) · tài liệu khoá (trích / viết lại) · nhóm tự viết · sinh có seed |
| Xử lý những bước gì | lọc __ · làm sạch __ · ẩn danh __ · chia __ (script: `…`) |
| Số dòng / số đoạn | __ |
| Phiên bản / ngày lấy | __ |
| Nhãn | thật · `synthetic` |
| Giới hạn | thiếu gì, lệch về phía nào |

**Data `synthetic` (nhóm tự sinh):** ghi cách sinh (prompt / script), seed, người kiểm, số dòng đã kiểm tay. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · [tên]

…
