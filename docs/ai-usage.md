# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | ChatGPT/Codex | Hỗ trợ viết luồng D1 và sửa phản hồi sau `run-2` | Kiểm bằng `python run.py check` và ca cục bộ; lượt AI thật sau sửa chưa chạy | Nhóm xác nhận người phụ trách |
| Prompt / thiết kế lời gọi mô hình | ChatGPT/Codex | Hỗ trợ tạo prompt phân loại JSON và cổng chính sách bằng code | Đối chiếu `spec.md` §4 và log `run-1`, `run-2` | Nhóm xác nhận người phụ trách |
| Đào data (viết script đếm, gợi ý nhãn) | ChatGPT/Codex | Viết script đếm và truy vết câu khảo sát diễn đạt lại | Script `evidence/derive_survey_cases.py`; cần nhóm kiểm tay nhãn nguồn | Nhóm xác nhận người phụ trách |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | ChatGPT/Codex | Diễn đạt lại lựa chọn từ 10 dòng khảo sát thành B21–B30 | Mỗi câu có `source` chỉ dòng; không gọi đó là lời nguyên văn | Nhóm xác nhận người phụ trách |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | ChatGPT/Codex | Soạn `eval/report.md`, `cost/cost-estimate.md`, `slides/demo-slides.html` | Nhóm cần đọc lại toàn bộ trước khi nộp | Nhóm xác nhận người phụ trách |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
