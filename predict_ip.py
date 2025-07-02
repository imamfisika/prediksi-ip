import pickle

# Load model
try:
    with open("model.pkl", "rb") as f:
        model, label_encoder = pickle.load(f)
except FileNotFoundError:
    print("❌ model.pkl tidak ditemukan!")
    exit(1)

# Minta input user
try:
    ip1 = float(input("Masukkan IP semester 1: "))
    ip2 = float(input("Masukkan IP semester 2: "))
    ip3 = float(input("Masukkan IP semester 3: "))
    ip4 = float(input("Masukkan IP semester 4: "))
except ValueError:
    print("❗ Input harus berupa angka desimal.")
    exit(1)

# Prediksi
predicted_class = model.predict([[ip1, ip2, ip3, ip4]])[0]
predicted_label = label_encoder.inverse_transform([predicted_class])[0]

print(f"Prediksi IP Semester 5 masuk dalam kategori: {predicted_label}")
