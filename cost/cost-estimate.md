# Chi phí khi dùng thật — mô phỏng 50 phiên

## Đầu vào

- Persona, tỷ lệ và quy mô 100/300/1.000 người: `cost/personas.yaml`; đều **tự ước tính** vì khảo sát n=30 không đo số lần dùng AI. Bình quân giả định 3,7 lời gọi/người/tháng.
- Tỷ lệ đạt dùng tính chi phí/task: **26/30 (87%)**, từ `eval/run-3.csv`, run ID `run-3@20261127-205753` (chạy bằng `gemini-3.1-flash-lite`). Đây là tỷ lệ trên benchmark, không phải tỷ lệ thực tế của người dùng.
- Giá Standard paid, USD/1 triệu token, xem 27/11/2026: [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.1-flash-lite) **$0,25 vào / $1,50 ra**; [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.1-pro-preview) **$2 vào / $12 ra** cho prompt ≤200.000 token. Token đo trên `gemini-3.1-flash-lite-preview`; Pro là kịch bản áp giá, chưa chạy model Pro.

## Kết quả mô phỏng

Nguồn trực tiếp: `cost/simulate-2-summary.md` và `cost/simulate-2.csv`; run ID **`simulate-2@20261128-140209`**, seed **42**, **50 phiên** (đo token trên `gemini-3.1-flash-lite-preview`, áp tỷ lệ đạt từ `run-3` trên `gemini-3.1-flash-lite`). Có **38 phiên không lỗi, 12 phiên lỗi** (24%). Khung **loại phiên lỗi khỏi trung bình**; vì thế bảng dưới phản ánh chi phí của phiên không lỗi và có thể đánh giá thấp chi phí vận hành khi phải gọi lại hoặc hỗ trợ thủ công. Giữ nguyên file mô phỏng và trace `traces/simulate-2.jsonl` (cùng bản chạy trước `simulate-1`).

| Persona | Phiên không lỗi | Lượt hỏi/phiên | Token vào/phiên | Token ra/phiên |
|---|---:|---:|---:|---:|
| Dùng ít | 22 | 1 | 98 | 22 |
| Dùng vừa | 15 | 2 | 198 | 44 |
| Dùng nhiều | 1 | 3 | 238 | 72 |

| Model áp giá (đo token trên `gemini-3.1-flash-lite-preview`) | USD/phiên | USD/task đạt | USD/câu hỏi đạt | 100 người/tháng | 300 người/tháng | 1.000 người/tháng | USD/người/tháng, cơ sở |
|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.1 Flash-Lite ($0,25 vào / $1,50 ra) | 0,000083 | 0,000096 | 0,000066 | 0,0209 | 0,0628 | 0,2095 | 0,00021 |
| Gemini 3.1 Pro Preview, áp giá giả định ($2,0 vào / $12,0 ra) | 0,00066 | 0,00077 | 0,00053 | 0,1676 | 0,5028 | 1,68 | 0,0017 |

Chi phí/task đạt = chi phí/phiên ÷ (26/30). Chi phí/câu hỏi đạt = chi phí/phiên ÷ 1,4 lượt hỏi trung bình/phiên ÷ (26/30). Bảng không gồm hosting, lưu trữ, thời gian người duyệt, chi phí gọi lại và chi phí xử lý phiên thất bại. Token đo trên `gemini-3.1-flash-lite-preview`, tính giá theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch.

## So với impact

`spec.md` §2 ước tính mức sàn 120 phút/tháng **trong 24 người khảo sát**; bảng chi phí giả định **300 người dùng** ở kịch bản cơ sở. Hai mẫu số khác nhau nên không tính lợi ích ròng trực tiếp. Chi phí model rất thấp trong mô phỏng ($0,00021/người/tháng ở mức cơ sở với Flash-Lite), nhưng **12/50 phiên lỗi** là rào cản đáng kể; cần cải thiện độ ổn định API và đo lại trên người dùng thật trước khi quyết định triển khai rộng.