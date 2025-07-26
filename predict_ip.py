import pickle
import pandas as pd

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

try:
    ip1 = float(input("Masukkan IP semester 1: "))
    ip2 = float(input("Masukkan IP semester 2: "))
    ip3 = float(input("Masukkan IP semester 3: "))
    ip4 = float(input("Masukkan IP semester 4: "))
    ip5 = float(input("Masukkan IP semester 5: "))
    ip6 = float(input("Masukkan IP semester 6: "))
    ip7 = float(input("Masukkan IP semester 7: "))
except ValueError:
    print("❗ Masukkan hanya angka desimal")
    exit(1)

input_data = pd.DataFrame([{
    'semester1': ip1,
    'semester2': ip2,
    'semester3': ip3,
    'semester4': ip4,
    'semester5': ip5,
    'semester6': ip6,
    'semester7': ip7,
}])

prediksi_ip8 = model.predict(input_data)[0]

print(f"Prediksi IP Semester 8: {prediksi_ip8:.2f}")