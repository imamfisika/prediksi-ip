import pickle

print("📦 Memuat model...")
try:
    with open("model.pkl", "rb") as f:
        model, label_encoder = pickle.load(f)
except FileNotFoundError:
    print("❌ File model.pkl tidak ditemukan!")
    exit(1)

print("✅ Model berhasil dimuat!")

try:
    ip1 = float(input("Masukkan IP semester 1: "))
    ip2 = float(input("Masukkan IP semester 2: "))
    ip3 = float(input("Masukkan IP semester 3: "))
except ValueError:
    print("❗ Input harus berupa angka (float)")
    exit(1)

predicted_class = model.predict([[ip1, ip2, ip3]])[0]
predicted_label = label_encoder.inverse_transform([predicted_class])[0]

print(f"🎯 Prediksi IP Semester 4 masuk dalam kategori: {predicted_label}")
