# Ứng dụng Vẽ và Xử lý Ảnh đơn giản với OpenCV

## 📌 Giới thiệu
Dự án này được xây dựng trong học phần **Xử lý ảnh và Thị giác máy tính**.  
Ứng dụng viết bằng Python, sử dụng các thư viện phổ biến như **OpenCV, Tkinter, Pillow, NumPy, Pygame**.  
Người dùng có thể chỉnh sửa, áp dụng bộ lọc, thao tác hình học và phát hiện đối tượng trên ảnh/video thông qua giao diện đồ họa thân thiện.

## ✨ Tính năng chính
- **Lọc ảnh**: Negative, Black–White, Sepia, Gaussian Blur, Median Blur, Emboss, Sketch, Oil Paint…
- **Chỉnh sửa ảnh**: Điều chỉnh độ sáng, kênh màu RGB, gamma, histogram, các phép toán hình thái học.
- **Thao tác hình học**: Xoay, lật, cắt, chèn ảnh, vẽ trực tiếp.
- **Phát hiện & nhận dạng**:
  - Phát hiện biên (Canny).
  - Nhận diện hình dạng cơ bản (tam giác, vuông, tròn…).
  - Nhận diện khẩu trang bằng mô hình YOLOv4-tiny.
- **Giao diện đồ họa (GUI)**: Xây dựng bằng Tkinter.
- **Nhạc nền**: Tích hợp Pygame mixer phát nhạc khi sử dụng ứng dụng.

## 🛠 Công nghệ sử dụng
- [Python 3.18](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://pillow.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [Pygame](https://www.pygame.org/)

## 📷 Giao diện
Một số hình ảnh minh họa giao diện và kết quả xử lý:

- Giao diện chính: ![Main UI](docs/images/ui_main.png)
- Bộ lọc ảnh: ![Filters](docs/images/filter_example.png)
- Phát hiện đối tượng: ![Detection](docs/images/detection_example.png)

## 🚀 Cài đặt và chạy
1. Clone repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
2. Cài đặt thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
3. Chạy ứng :
   ```bash
   python main.py

---
## 📬 **Liên hệ**  
- **Tác giả**: [Nguyễn Văn Hạnh]  
- **Email**: [vhanh1366@gmail.com]  

---
