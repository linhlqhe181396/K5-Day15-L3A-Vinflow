# Tóm tắt mô phỏng simulate-2@20261128-140209

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 22 | 1 | 98 | 22 | 1.0 | 0.8 |
| dung_vua | 15 | 2 | 198 | 44 | 2.0 | 1.9 |
| dung_nhieu | 1 | 3 | 238 | 72 | 3.0 | 8.0 |

Tỉ lệ đạt dùng để tính: 26/30 (87%) — lượt run-3@20261127-205753

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-3.csv (--rate-from). ⚠️ Lượt này chạy bằng gemini-3.1-flash-lite, mô phỏng đo trên gemini-3.1-flash-lite-preview — khác model.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (100 người) | Chi phí / tháng — cơ sở (300 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.000083 | $0.000096 | $0.000066 | $0.0209 | $0.0628 | $0.2095 | $0.00021 |
| gemini-3.1-pro-preview (vào 2.0 · ra 12.0 $/1M) | $0.00066 | $0.00077 | $0.00053 | $0.1676 | $0.5028 | $1.68 | $0.0017 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.4) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.1-flash-lite-preview. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 12/50.
