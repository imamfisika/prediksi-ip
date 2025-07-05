import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Input IP dari user
try:
    ip1 = float(input("Masukkan IP semester 1: "))
    ip2 = float(input("Masukkan IP semester 2: "))
    ip3 = float(input("Masukkan IP semester 3: "))
    ip4 = float(input("Masukkan IP semester 4: "))
except ValueError:
    print("❗ Masukkan hanya angka desimal")
    exit(1)



input_data = pd.DataFrame([{
    'semester1': ip1,
    'semester2': ip2,
    'semester3': ip3,
    'semester4': ip4
}])

prediksi_ip5 = model.predict(input_data)[0]

print(f"Prediksi IP Semester 5: {prediksi_ip5:.2f}")