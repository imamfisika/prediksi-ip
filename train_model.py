import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
import pickle
import os

df = pd.read_csv("data4.csv")
df = df.fillna(df.mean())

os.makedirs("models", exist_ok=True)

# Melatih model regresi untuk semester 2–8
for sem in range(2, 9):
    fitur = [f"semester{i}" for i in range(1, sem)]
    X = df[fitur]
    y = df[f"semester{sem}"]

    model = LinearRegression()
    model.fit(X, y)

    with open(f"models/model_sem{sem}.pkl", "wb") as f:
        pickle.dump(model, f) 

# Kategorisasi IP semester 2–8
def ip_to_label(ip):
    if ip > 3.5:
        return "Berprestasi"
    elif ip >= 3.01 and ip <= 3.5:
        return "Cukup Berprestasi"
    else:
        return "Kurang Berprestasi"

# Buat label kategori untuk semua semester
for sem in range(2, 9):
    df[f'kategori{sem}'] = df[f'semester{sem}'].apply(ip_to_label)

# Train Naive Bayes untuk kategori semester 2–8
for sem in range(2, 9):
    fitur = [f"semester{i}" for i in range(1, sem)]
    X = df[fitur]
    y = df[f"kategori{sem}"]

    model = GaussianNB()
    model.fit(X, y)

    with open(f"models/nb_model_sem{sem}.pkl", "wb") as f:
        pickle.dump(model, f)


print("✅ Semua model berhasil dilatih dan disimpan.")