# Prediksi IP Mahasiswa Menggunakan API FastAPI

Proyek ini menyediakan REST API untuk memprediksi **IP (Indeks Prestasi) semester ke-5 mahasiswa** berdasarkan IP semester 1 hingga 4. Model dilatih menggunakan algoritma **Linear Regression** dari scikit-learn.

---

## 🔍 Algoritma yang Digunakan

### Linear Regression

Model ini digunakan untuk memprediksi nilai kontinu (IP semester 5) berdasarkan kombinasi fitur numerik (IP semester 1–4). Linear Regression berusaha mencari garis (atau bidang) terbaik yang meminimalkan **Mean Squared Error (MSE)** antara prediksi dan nilai aktual.

- **Input fitur:** `semester1`, `semester2`, `semester3`, `semester4`
- **Output prediksi:** nilai `semester5` (dalam angka desimal)

---

## 🚀 Cara Menjalankan API

### 1. Clone repositori dan pindah ke folder proyek

```bash
git clone <url-repo>
cd project
```

### 2. Build Docker image

```bash
docker-compose build
```

### 3. Jalankan API

```bash
docker-compose up
```

API akan tersedia di:

```
http://localhost:8000
```

---

## 📡 Endpoint API

### 🔹 `GET /`

- Cek apakah API aktif
- **Response:**

```json
{"message": "API prediksi IP siap digunakan."}
```

### 🔹 `POST /predict`

- Prediksi IP semester 5 berdasarkan input IP semester 1–4

#### 🔸 Request Body

```json
{
  "semester1": 3.0,
  "semester2": 3.1,
  "semester3": 3.2,
  "semester4": 3.3
}
```

#### 🔸 Response

```json
{
  "prediksi_ip_semester5": 3.42
}
```

---

## 📁 File Penting

| Nama File            | Deskripsi                                                          |
| -------------------- | ------------------------------------------------------------------ |
| `train_model.py`     | Melatih model regresi dari `data.csv` dan menyimpan ke `model.pkl` |
| `predict_ip.py`      | Prediksi IP semester ke-5 via input manual CLI                     |
| `api.py`             | API FastAPI untuk prediksi IP via HTTP                             |
| `data.csv`           | Dataset IP semester 1–5                                            |
| `Dockerfile`         | Build image Python + API                                           |
| `docker-compose.yml` | Jalankan container dengan expose port 8000                         |
| `requirements.txt`   | Daftar dependency (pandas, scikit-learn, fastapi, dll)             |

---

## ⚠️ Catatan

- Pastikan model sudah dilatih (`train_model.py`) sebelum menjalankan API.
- API hanya memprediksi, tidak menyimpan data ke database.

---

## 📬 Kontak

Proyek ini dikembangkan untuk keperluan pembelajaran. Jika ada pertanyaan, silakan hubungi pengembang.

