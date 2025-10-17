# 🧾 BÁO CÁO HUẤN LUYỆN MÔ HÌNH YOLOv8

## ⚙️ Thông tin huấn luyện

| Thông số | Giá trị |
|-----------|----------|
| **Thời gian huấn luyện** | 55 phút |
| **Số lượng mẫu huấn luyện (train_sample)** | 530 ảnh |
| **Kích thước ảnh (image_size)** | 1280 × 1280 |
| **Dung lượng VRAM tối đa sử dụng** | 6.9 GB |
| **Thiết bị** | Tesla T4 (15 GB VRAM) |
| **Framework** | Ultralytics YOLOv8.3.215 |
| **Python / Torch / CUDA** | 3.12.12 / 2.8.0+cu126 / CUDA:0 |

---

## 🧩 Mô hình tổng quan

| Thông tin | Giá trị |
|------------|----------|
| **Kiến trúc (fused)** | 72 layers |
| **Số tham số (parameters)** | 3,006,428 |
| **Số gradient** | 0 |
| **Tốc độ xử lý (GFLOPs)** | 8.1 |

---

## 📊 KẾT QUẢ ĐÁNH GIÁ TRÊN TẬP VALIDATION

| Lớp (Class) | Ảnh (Images) | Đối tượng (Instances) | Precision (P) | Recall (R) | mAP@50 | mAP@50–95 |
|--------------|---------------|------------------------|----------------|-------------|-----------|-------------|
| **Tất cả (All)** | 66 | 70 | **0.928** | **0.899** | **0.904** | **0.783** |
| **RB19** | 28 | 28 | 0.949 | 0.750 | 0.822 | 0.625 |
| **Quyt_kiem_sy** | 17 | 17 | 0.933 | 1.000 | 0.969 | 0.892 |
| **Tao_thien_xa** | 13 | 13 | 0.845 | 0.846 | 0.829 | 0.746 |
| **Thom_giac_dau** | 12 | 12 | 0.985 | 1.000 | 0.995 | 0.869 |

> 💨 **Tốc độ inference trung bình:**  
> - Preprocess: 0.8ms  
> - Inference: 9.5ms  
> - Postprocess: 25.5ms / ảnh  

---

## 🧪 KẾT QUẢ ĐÁNH GIÁ TRÊN TẬP TEST

| Lớp (Class) | Ảnh (Images) | Đối tượng (Instances) | Precision (P) | Recall (R) | mAP@50 | mAP@50–95 |
|--------------|---------------|------------------------|----------------|-------------|-----------|-------------|
| **Tất cả (All)** | 33 | 30 | **0.872** | **0.890** | **0.865** | **0.727** |
| **RB19** | 9 | 9 | 0.765 | 0.778 | 0.713 | 0.652 |
| **Quyt_kiem_sy** | 10 | 10 | 0.887 | 0.783 | 0.827 | 0.672 |
| **Tao_thien_xa** | 6 | 6 | 0.840 | 1.000 | 0.924 | 0.791 |
| **Thom_giac_dau** | 5 | 5 | 0.995 | 1.000 | 0.995 | 0.792 |

> 💨 **Tốc độ inference trên test:**  
> - Preprocess: 11.8ms  
> - Inference: 33.1ms  
> - Postprocess: 1.7ms / ảnh  
