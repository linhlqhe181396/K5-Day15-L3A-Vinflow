# Chi phí khi dùng thật — mô phỏng 50 phiên

## Đầu vào

- Persona, tỷ lệ và quy mô 100/300/1.000 người: `cost/personas.yaml`; đều **tự ước tính** vì khảo sát n=30 không đo số lần dùng AI. Bình quân giả định 3,7 lời gọi/người/tháng.
- Tỷ lệ đạt dùng tính chi phí/task: **26/30 (87%)**, từ `eval/run-3.csv`, run ID `run-3@20261127-205753`. Đây là tỷ lệ trên benchmark, không phải tỷ lệ thực tế của người dùng.
- Giá Standard paid, USD/1 triệu token, xem 27/11/2026: [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.1-flash-lite) **$0,25 vào / $1,50 ra**; [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.1-pro-preview) **$2 vào / $12 ra** cho prompt ≤200.000 token. Token chỉ đo bằng Flash-Lite; Pro là kịch bản áp giá, chưa chạy model Pro.

## Kết quả mô phỏng

Nguồn trực tiếp: `cost/simulate-1-summary.md` và `cost/simulate-1.csv`; run ID **`simulate-1@20261127-211609`**, seed **42**, **50 phiên**. Có **36 phiên không lỗi, 14 phiên lỗi** (28%). Khung **loại phiên lỗi khỏi trung bình**; vì thế bảng dưới phản ánh chi phí của phiên không lỗi và có thể đánh giá thấp chi phí vận hành khi phải gọi lại hoặc hỗ trợ thủ công. Giữ nguyên file mô phỏng và trace `traces/simulate-1.jsonl`.

| Persona | Phiên không lỗi | Lượt hỏi/phiên | Token vào/phiên | Token ra/phiên |
|---|---:|---:|---:|---:|
| Dùng ít | 18 | 1 | 99 | 22 |
| Dùng vừa | 16 | 2 | 204 | 43 |
| Dùng nhiều | 2 | 3 | 264 | 68 |

| Model áp giá | USD/phiên | USD/task đạt | USD/câu hỏi đạt | 100 người/tháng | 300 người/tháng | 1.000 người/tháng | USD/người/tháng, cơ sở |
|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini 3.1 Flash-Lite | 0,000089 | 0,00010 | 0,000066 | 0,0210 | 0,0629 | 0,2097 | 0,00021 |
| Gemini 3.1 Pro Preview, áp giá giả định | 0,00071 | 0,00082 | 0,00053 | 0,1678 | 0,5033 | 1,68 | 0,0017 |

Chi phí/task đạt = chi phí/phiên ÷ (26/30). Chi phí/câu hỏi đạt = chi phí/phiên ÷ 1,6 lượt hỏi trung bình/phiên ÷ (26/30). Bảng không gồm hosting, lưu trữ, thời gian người duyệt, chi phí gọi lại và chi phí xử lý phiên thất bại. Giá Pro áp vào token Flash-Lite nên chỉ là kịch bản so sánh.

## So với impact

`spec.md` §2 ước tính mức sàn 120 phút/tháng **trong 24 người khảo sát**; bảng chi phí giả định **300 người dùng** ở kịch bản cơ sở. Hai mẫu số khác nhau nên không tính lợi ích ròng trực tiếp. Chi phí model thấp trong mô phỏng, nhưng **14/50 phiên lỗi** là rào cản đáng kể; cần cải thiện độ ổn định và đo lại trên người dùng thật trước khi quyết định triển khai rộng.
