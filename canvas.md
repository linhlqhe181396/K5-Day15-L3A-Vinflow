# Canvas — [Vinflow] · Track D

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số đầu tiên, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | Track D (E-commerce) — Xử lý khiếu nại đơn giao đồ ăn thiếu món / giao trễ trong hạn mức |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Người đặt đồ ăn qua ứng dụng gặp sự cố thiếu món hoặc giao trễ |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Người đặt đồ ăn — đang khiếu nại đơn thiếu món hoặc giao trễ — vướng việc bot trả lời theo menu cứng hoặc xử lý chậm/không nhất quán — dẫn đến mất thời gian, bức xúc hoặc mất quyền lợi chính đáng |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | Giả thuyết: người đặt đồ ăn qua app gặp khó khăn khi khiếu nại thiếu món hoặc giao trễ vì phải cung cấp thông tin nhiều lần hoặc chờ phản hồi. Nguồn kiểm chứng pain: khảo sát/phỏng vấn người mua và review công khai 1–3 sao trên Google Play / App Store (chưa có số liệu hay trích dẫn từ người dùng thật). Dữ liệu để thử AI: [Food Delivery Support Tickets](https://huggingface.co/datasets/OrSabbach/food-delivery-support-tickets) gồm 10.153 ca **giả lập**, trong đó 1.309 ca `missing_item` và 1.309 ca `late_delivery`; các số này chỉ mô tả bộ dữ liệu, không chứng minh tần suất sự cố thực tế. |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Người đặt đồ ăn nhận đơn thiếu món hoặc giao trễ → hệ thống đối chiếu đơn, chính sách và hạn mức để tự động hoàn phần thiếu/cấp voucher trong hạn mức hoặc chuyển nhân viên → người dùng nhận phương án xử lý rõ ràng hoặc biết lý do chuyển người |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | Tự xử lý và đề xuất phương án trong hạn mức cho ca rõ ràng; vượt hạn mức, khiếu nại bất thường, doạ bóc phốt hoặc có dấu hiệu mất an toàn thực phẩm thì chuyển nhân viên — vì hoàn tiền/voucher sai làm thiệt hại ngân sách sàn/quán hoặc mất niềm tin khách hàng |
| 7 | Phân công có tên | [Lê Quang Linh - Đội trưởng]: repo, `TEAMS.md`, `canvas.md`, luồng chính; [Nguyễn Hữu Tiến]: bằng chứng, `spec.md`; [Mai Tuấn Anh]: tools, chặn hạn mức, model thật, chi phí; [Nguyễn Quang Duy]: bộ test/metric, báo cáo đánh giá, slide |
| — | *(CP2)* Đã đổi gì so với CP1 | Bổ sung thông tin tập dữ liệu `Food Delivery Support Tickets` (10.153 ca giả lập, gồm 1.309 `missing_item` và 1.309 `late_delivery`) vào dòng 4 và tách bạch rõ nguồn kiểm chứng pain thực tế với dữ liệu chạy thử. Chuẩn bị chốt chuẩn "đạt" ở `spec.md` §7, sơ đồ §4, bộ test/metric/DATA_CARD và khung luồng AI giả trước 19:30. |
