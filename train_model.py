import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv("data3.csv")

# Hapus data yang semester5-nya 0 (tidak valid)
df = df[df['semester5'] > 0]


# Fitur dan target (prediksi IP semester ke-5)
X = df[['semester1', 'semester2', 'semester3', 'semester4']]
y = df['semester5']  # sekarang nilai float

# Latih model regresi
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)

print(f"📉 MSE (mean squared error): {mse:.4f}")

# Simpan model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model regresi berhasil disimpan ke 'model.pkl'")
