# Tóm tắt mô phỏng simulate-1@20261127-211609

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 18 | 1 | 99 | 22 | 1.0 | 0.7 |
| dung_vua | 16 | 2 | 204 | 43 | 2.0 | 2.0 |
| dung_nhieu | 2 | 3 | 264 | 68 | 3.0 | 4.5 |

Tỉ lệ đạt dùng để tính: 26/30 (87%) — lượt run-3@20261127-205753

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-3.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (100 người) | Chi phí / tháng — cơ sở (300 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.000089 | $0.00010 | $0.000066 | $0.0210 | $0.0629 | $0.2097 | $0.00021 |
| gemini-3.1-pro-preview (vào 2.0 · ra 12.0 $/1M) | $0.00071 | $0.00082 | $0.00053 | $0.1678 | $0.5033 | $1.68 | $0.0017 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.6) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.1-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 14/50.
