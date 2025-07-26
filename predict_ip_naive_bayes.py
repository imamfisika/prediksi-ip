import pickle

try:
    with open("model.pkl", "rb") as f:
        model, label_encoder = pickle.load(f)
except FileNotFoundError:
    print("❌ model.pkl tidak ditemukan!")
    exit(1)

try:
    ip1 = float(input("Masukkan IP semester 1: "))
    ip2 = float(input("Masukkan IP semester 2: "))
    ip3 = float(input("Masukkan IP semester 3: "))
    ip4 = float(input("Masukkan IP semester 4: "))
    ip5 = float(input("Masukkan IP semester 5: "))
    ip6 = float(input("Masukkan IP semester 6: "))
    ip7 = float(input("Masukkan IP semester 7: "))
except ValueError:
    print("❗ Input harus berupa angka desimal.")
    exit(1)

predicted_class = model.predict([[ip1, ip2, ip3, ip4, ip5, ip6, ip7]])[0]
predicted_label = label_encoder.inverse_transform([predicted_class])[0]

print(f"🎯 Prediksi IP Semester 8 masuk dalam kategori: {predicted_label}")