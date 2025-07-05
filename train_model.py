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

df["kategori5"] = df["semester5"].apply(ip_to_label)
X_nb = df[["semester1", "semester2", "semester3", "semester4"]]
y_nb = df["kategori5"]

nb_model = GaussianNB()
nb_model.fit(X_nb, y_nb)

with open("models/model_nb_sem5.pkl", "wb") as f:
    pickle.dump(nb_model, f)

print("✅ Semua model berhasil dilatih dan disimpan.")
