# Tổng hợp bằng chứng pain — D1

## 1. Nguồn đã dùng

| Nguồn | Quy mô | Vai trò |
|---|---:|---|
| `data/raw/survey.csv` | 30 phiếu, ghi ngày 27/11/2026 | Bằng chứng tự báo cáo về sự cố và trải nghiệm khiếu nại của người trả lời |
| [Food Delivery Support Tickets](https://huggingface.co/datasets/OrSabbach/food-delivery-support-tickets), lưu tại `data/raw/food-delivery-support-tickets.csv` | 10.153 ca **giả lập** | Dữ liệu phát triển và thử khả năng nhận diện loại khiếu nại; không phải bằng chứng pain của người thật |

Nhóm không dùng phỏng vấn. Chưa có tài liệu ghi kênh phát khảo sát, đối tượng được mời và cách xác nhận 30 người trả lời đều ở ngoài nhóm; cần bổ sung thông tin đó nếu dùng ngưỡng khảo sát ≥20 người ngoài nhóm của bài.

## 2. Cách đếm khảo sát

Mẫu số là **30 dòng trả lời** trong `data/raw/survey.csv`, không tính dòng tiêu đề. Đếm số phiếu chọn từng phương án trong cột tương ứng; mỗi câu hỏi dưới đây là một lựa chọn nên các phương án cùng câu không cộng trùng. Tỉ lệ = số phiếu / 30 × 100, làm tròn một chữ số thập phân. File gốc có dấu thời gian nhưng không có tên, email hay số điện thoại. Với câu hỏi thời gian xử lý, chỉ xét **19 phiếu cho biết đã gửi khiếu nại**.

| Câu hỏi / kết quả | Số phiếu | Tỉ lệ trong 30 phiếu |
|---|---:|---:|
| Đặt đồ ăn/đồ uống qua app trong tháng qua: Có | 30/30 | 100% |
| Gặp thiếu món/topping | 6/30 | 20,0% |
| Gặp giao trễ | 13/30 | 43,3% |
| Gặp cả thiếu món và giao trễ | 11/30 | 36,7% |
| Đã khiếu nại nhưng xử lý chậm/chưa thỏa đáng/phải làm lại | 13/30 | 43,3% |
| Không gửi khiếu nại vì thấy rườm rà/mất thời gian/không kỳ vọng được giải quyết nhanh | 11/30 | 36,7% |
| Đã khiếu nại và được xử lý xong | 6/30 | 20,0% |
| Trong số người đã gửi khiếu nại, chọn xử lý chậm/chưa thỏa đáng/phải làm lại | 13/19 | 68,4% |
| Điểm vướng nhất: cung cấp lại thông tin/chứng cứ hoặc chờ phản hồi lâu | 11/30 | 36,7% |
| Điểm vướng nhất: mức hoàn/voucher chưa khớp thiệt hại hoặc không rõ lý do | 11/30 | 36,7% |
| Muốn tự động hoàn phần thiếu hoặc cấp voucher rõ ràng cho ca đơn giản | 17/30 | 56,7% |

Trong 19 người cho biết đã gửi khiếu nại, thời gian tự ước lượng: dưới 5 phút **3/19**, 5–15 phút **8/19**, 15–30 phút **4/19**, trên 30 phút **4/19**. Đây là khoảng thời gian tự báo cáo, không phải thời gian đo từ hệ thống; không tính trung bình từ các khoảng này.

**Lưu ý về mẫu:** Cả 30 phiếu đều chọn đã gặp thiếu món, giao trễ hoặc cả hai. Không rõ đây là kết quả của việc tuyển đúng người đã gặp sự cố hay cách phát khảo sát, nên **không suy ra tỉ lệ gặp sự cố trong toàn bộ người đặt đồ ăn**. Câu hỏi về thời gian cũng được trả lời bởi 11 người không gửi khiếu nại; các phiếu đó được loại khỏi phép đếm thời gian ở trên.

## 3. Dữ liệu giả lập để thử D1

Chạy `python evidence/count.py` cho kết quả: `missing_item` **1.309/10.153 (12,9%)**, `late_delivery` **1.309/10.153 (12,9%)**; gộp hai loại **2.618/10.153 (25,8%)**. Cách đếm và năm ví dụ có `id` ở `evidence/data-mining.md`. Đây là phân bố do tác giả chủ động tạo, **không phải tần suất khiếu nại thực tế**.

## 4. Trích dẫn và giới hạn

`data/raw/survey.csv` chỉ lưu **đáp án chọn sẵn**, không có câu trả lời tự do để trích nguyên văn từ người dùng. Các cụm trong bảng trên là nội dung phương án khảo sát, không được ghi thành lời kể hoặc phỏng vấn. Năm ví dụ trong `evidence/data-mining.md` là câu do mô hình tạo, không phải trích dẫn người thật.

Khảo sát cho thấy trong **nhóm 30 người đã trả lời**, có người gặp khó khi gửi hoặc theo dõi khiếu nại; **24/30** chọn một trong hai phương án “xử lý chậm/chưa thỏa đáng/phải làm lại” hoặc “không gửi vì thấy rườm rà/mất thời gian/không kỳ vọng”. Điều này hỗ trợ giả thuyết pain của D1 **trong mẫu khảo sát này**. Chưa biết mẫu có đại diện cho người dùng app nói chung hay không, và chưa có bằng chứng độc lập về thời gian xử lý thực tế hay mức bồi thường phù hợp.
