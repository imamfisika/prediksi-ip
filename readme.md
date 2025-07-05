# Prediksi IP Mahasiswa Menggunakan API FastAPI

Proyek ini menyediakan REST API untuk memprediksi **IP (Indeks Prestasi) mahasiswa** untuk semester 2 hingga 5 berdasarkan nilai IP semester sebelumnya. Prediksi dapat berupa:

1. **Prediksi numerik** menggunakan **Linear Regression**
2. **Prediksi kategori** menggunakan **Naive Bayes** (rendah, sedang, tinggi — khusus semester 5)

---

## 🔍 Algoritma yang Digunakan

### 1. Linear Regression

Model ini digunakan untuk memprediksi nilai kontinu IP semester 2 hingga 5. Masing-masing semester memiliki model yang berbeda dengan fitur input sebagai berikut:

| Prediksi semester | Fitur input              |
| ----------------- | ------------------------ |
| Semester 2        | `semester1`              |
| Semester 3        | `semester1`, `semester2` |
| Semester 4        | `semester1–3`            |
| Semester 5        | `semester1–4`            |

### 2. Naive Bayes (GaussianNB)

Model klasifikasi khusus untuk IP semester 5 dalam 3 kategori:

- **tinggi** (≥ 3.5)
- **sedang** (≥ 2.75 dan < 3.5)
- **rendah** (< 2.75)

---

## 🚀 Cara Menjalankan API dengan Docker

### 1. Clone repositori dan pindah ke folder proyek

```bash
git clone <url-repo>
cd project
```

### 2. Jalankan API

```bash
docker-compose up --build
```

API akan tersedia di:

```
http://localhost:8080
```

---

## 📡 Endpoint API

### 🔹 `GET /`

- Cek apakah API aktif
- **Response:**

```json
{"message": "API prediksi IP aktif."}
```

### 🔹 `POST /predict/{semester}`

- Prediksi IP semester ke-`n` berdasarkan input semester sebelumnya
- **Parameter URL:** `semester` (2 hingga 5)

#### 🔸 Request Body (semua semester input)

```json
{
  "semester1": 3.0,
  "semester2": 3.1,
  "semester3": 3.2,
  "semester4": 3.3
}
```

#### 🔸 Response (contoh prediksi semester 3)

```json
{
  "prediksi_ip_semester3": 3.18
}
```

### 🔹 `POST /predict/5/kategori`

- Prediksi kategori IP semester 5 (rendah, sedang, tinggi)
- **Input:** IP semester 1–4

---

## 📁 File Penting

| Nama File            | Deskripsi                                                                 |
| -------------------- | ------------------------------------------------------------------------- |
| `train_model.py`     | Melatih model regresi untuk semester 2–5 dan naive bayes untuk semester 5 |
| `api.py`             | API FastAPI dengan endpoint fleksibel per semester                        |
| `data.csv`           | Dataset IP mahasiswa semester 1–5                                         |
| `Dockerfile`         | Image Python + pelatihan model + API                                      |
| `docker-compose.yml` | Menjalankan container dan expose port                                     |
| `requirements.txt`   | Dependency proyek                                                         |

---

## ⚠️ Catatan

- Pastikan `data.csv` tersedia sebelum build agar model dapat dilatih.
- Prediksi hanya berjalan jika model sudah tersedia.
- Dokumentasi Swagger tersedia di `http://localhost:8080/docs`

---

## 📬 Kontak

Proyek ini dikembangkan untuk keperluan pembelajaran. Jika ada pertanyaan, silakan hubungi pengembang.
