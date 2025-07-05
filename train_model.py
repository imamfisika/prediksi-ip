import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
import pickle
import os

df = pd.read_csv("data3.csv")
df = df.dropna()

# Siapkan direktori penyimpanan model
os.makedirs("models", exist_ok=True)

# Melatih model regresi untuk semester 2–5
for sem in range(2, 6):
    fitur = [f"semester{i}" for i in range(1, sem)]
    X = df[fitur]
    y = df[f"semester{sem}"]

    model = LinearRegression()
    model.fit(X, y)

    with open(f"models/model_sem{sem}.pkl", "wb") as f:
        pickle.dump(model, f)

# Kategorisasi IP semester 5
def ip_to_label(ip):
    if ip >= 3.5:
        return "tinggi"
    elif ip >= 2.75:
        return "sedang"
    else:
        return "rendah"

# Buat label kategori untuk semua semester
for sem in range(2, 6):
    df[f'kategori{sem}'] = df[f'semester{sem}'].apply(ip_to_label)

# Train Naive Bayes untuk kategori semester 2–5
for sem in range(2, 6):
    fitur = [f"semester{i}" for i in range(1, sem)]
    X = df[fitur]
    y = df[f"kategori{sem}"]

    model = GaussianNB()
    model.fit(X, y)

    with open(f"models/nb_model_sem{sem}.pkl", "wb") as f:
        pickle.dump(model, f)



print("✅ Semua model berhasil dilatih dan disimpan.")
