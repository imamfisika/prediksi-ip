import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load data
df = pd.read_csv("data3.csv")

# Fitur dan target (prediksi IP semester ke-5)
X = df[['semester1', 'semester2', 'semester3', 'semester4']]
y = df['semester5']  # sekarang nilai float

# Latih model regresi
model = LinearRegression()
model.fit(X, y)

# Simpan model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model regresi berhasil disimpan ke 'model.pkl'")
