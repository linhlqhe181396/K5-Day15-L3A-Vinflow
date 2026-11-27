# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử và UI | ChatGPT/Codex | Hỗ trợ viết luồng D1, sửa sau `run-2`, dựng `demo.py` và `web/` | Đã chạy `run-3` bằng Gemini thật; Linh và Tuấn Anh cần tự kiểm, giải thích được luồng | Linh (UI/repo), Tuấn Anh (agent/model) |
| Prompt / thiết kế lời gọi mô hình | ChatGPT/Codex | Hỗ trợ prompt phân loại JSON và chặn hạn mức bằng code | Đối chiếu `spec.md` §4 với `codebase/agent.py`, `ai.py` và `tools.py` | Tuấn Anh |
| Đào data (script đếm, nguồn câu thử) | ChatGPT/Codex | Viết script đếm và truy vết 10 câu khảo sát diễn đạt lại | `evidence/derive_survey_cases.py`; Tiến cần kiểm các dòng nguồn và cách phát khảo sát | Tiến |
| Phỏng vấn / khảo sát | Không dùng AI để tạo phiếu trả lời | Form thật do nhóm cung cấp; không có phỏng vấn | Giữ đúng lựa chọn trên CSV; không bịa lời kể tự do | Tiến |
| Viết câu thử (benchmark) | ChatGPT/Codex | Diễn đạt lại lựa chọn từ 10 dòng khảo sát thành B21–B30 | Mỗi câu có `source` chỉ dòng; Duy rà đầu vào và tiêu chí, không gọi là lời nguyên văn | Duy |
| Sinh data `synthetic` | Dataset giả lập của tác giả trên Hugging Face; nhóm tự viết đơn/chính sách mẫu | Không tạo dữ liệu người thật | Ghi rõ nhãn giả lập và hạn mức tự ước tính trong data card | Tiến, Tuấn Anh |
| Chấm cột `pass` | ChatGPT/Codex hỗ trợ đề xuất 1/0 và ghi chú cho lượt chạy | Không thay đổi output/expected/trace | Duy cần rà thủ công 30 câu `run-3`; Linh chấm độc lập 5 câu nếu không viết §7. Chưa ghi là hoàn tất. | Duy, Linh |
| Slide, văn bản | ChatGPT/Codex | Soạn `eval/report.md`, `cost/cost-estimate.md`, `slides/demo-slides.html` | Duy và nhóm cần đọc lại, xuất PDF và tự trình bày | Duy |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
