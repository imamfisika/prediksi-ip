import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("data3.csv")

# Kategorisasi IP menjadi label
def ip_to_label(ip):
    if ip < 2.5:
        return "rendah"
    elif ip < 3.25:
        return "sedang"
    else:
        return "tinggi"

df['label'] = df['semester5'].apply(ip_to_label)

# Fitur dan label
X = df[['semester1', 'semester2', 'semester3', 'semester4']]
y = df['label']

# Encode label
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Latih model
model = GaussianNB()
model.fit(X, y_encoded)

# Simpan model dan encoder
with open("model.pkl", "wb") as f:
    pickle.dump((model, le), f)

print("✅ Model berhasil disimpan ke 'model_naive_bayes.pkl'")
