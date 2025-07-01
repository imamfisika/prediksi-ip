import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Klasifikasi label IP ke kategori
def ip_to_label(ip):
    if ip < 2.5:
        return "rendah"
    elif ip < 3.25:
        return "sedang"
    else:
        return "tinggi"

df['label'] = df['label_ip_semester_4'].apply(ip_to_label)

# Fitur dan label
X = df[['ip_semester_1', 'ip_semester_2', 'ip_semester_3']]
y = df['label']

# Encode label
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train model
model = GaussianNB()
model.fit(X, y_encoded)

# Simpan model dan label encoder
with open("model.pkl", "wb") as f:
    pickle.dump((model, le), f)

print("Model berhasil dilatih dan disimpan sebagai 'model.pkl'")
