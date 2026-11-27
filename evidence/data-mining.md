# Đào dữ liệu — bộ khiếu nại giao đồ ăn giả lập

## 1. Nguồn và cách đếm

- Nguồn: [Food Delivery Support Tickets](https://huggingface.co/datasets/OrSabbach/food-delivery-support-tickets), file `data/raw/food-delivery-support-tickets.csv`; 10.153 ca do mô hình tạo bằng tiếng Anh. Không có khoảng ngày phát sinh khiếu nại thật. Giới hạn và giấy phép ghi tại `data/DATA_CARD.md`.
- Đơn vị đếm: **một dòng CSV**; mẫu số là toàn bộ 10.153 dòng, không phải số người hay số đơn hàng thực tế. Không lọc dòng nào. Đếm theo cột `category` do tác giả dataset gán khi tạo dữ liệu.
- Chạy lại: `python evidence/count.py` (chỉ dùng thư viện chuẩn Python). Tỉ lệ = số dòng thuộc nhóm / 10.153 × 100, làm tròn một chữ số thập phân.

## 2. Đọc mẫu trước khi đếm

Đã xem cấu trúc 10 cột và các dòng đầu. `customer_message` mô tả vấn đề, `category` là một trong tám loại sự cố. Các kiểu thấy được: báo thiếu một thành phần hoặc món phụ; báo đơn đến muộn kèm số phút; có ca ngoài lát cắt D1 như giao nhầm món hoặc thanh toán. Mẫu đôi khi thiếu nhất quán về quán/món; đây là dữ liệu giả lập, không phải lời kể của người dùng thật.

## 3. Kết quả

| Nhóm | x / N | Tỉ lệ | Ý nghĩa |
|---|---:|---:|---|
| Thiếu món (`missing_item`) | 1.309 / 10.153 | 12,9% | Ca giả lập dùng để thử nhận diện thiếu món |
| Giao trễ (`late_delivery`) | 1.309 / 10.153 | 12,9% | Ca giả lập dùng để thử nhận diện giao trễ |
| Hai loại trong lát cắt D1 | 2.618 / 10.153 | 25,8% | Tập ứng viên để chọn câu thử, **không phải tần suất sự cố thực tế** |
| Sáu loại khác | 7.535 / 10.153 | 74,2% | Có thể thử chuyển kênh ngoài phạm vi |

## 4. Năm ví dụ từ file gốc

Các câu dưới đây giữ nguyên tiếng Anh; `id` là mã dòng trong CSV, không phải mã người dùng.

1. `id=1`, `missing_item`: “The chicken shawarma from the vegan cafe was missing the tahini sauce. Only the meat and pita arrived.”
2. `id=6`, `late_delivery`: “I ordered a California roll from the burger joint in Austin. It was 115 minutes late, and I was disappointed.”
3. `id=12`, `late_delivery`: “The pad thai from the ramen shop in Atlanta was about 98 minutes late, and I missed a planned meal because of it. This is unacceptable.”
4. `id=18`, `missing_item`: “I ordered the pad thai from the Mediterranean grill in Portland, but only the main dish was in the bag and the extra side was missing.”
5. `id=34`, `missing_item`: “My order from the Indian restaurant was missing the chana masala I paid for. Only the biryani arrived.”

## 5. Giới hạn và kết luận

Dataset được tạo có chủ đích với các nhóm gần cân bằng; tỉ lệ 12,9% là tỉ lệ **trong bộ dữ liệu**, không đo xác suất khách hàng gặp thiếu món hay giao trễ. Dataset không cho biết khách thật có ngại khiếu nại, phải cung cấp thông tin nhiều lần, chờ bao lâu, hay mất quyền lợi ra sao. `urgency` và `sentiment` được tác giả đánh giá là nhãn không đáng tin; `resolution` không phải quyết định hoàn tiền chuẩn. Không dùng các câu này làm trích dẫn người dùng thật. Với nguồn duy nhất này, nhóm chỉ có thể kết luận rằng **có đủ ca giả lập để thử bước phân loại D1**, chưa kiểm chứng được giả thuyết pain trong `canvas.md`.
