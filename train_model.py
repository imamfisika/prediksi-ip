from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import pickle

df = pd.read_csv("data3.csv")
df = df[df['semester5'] > 0]

# Fitur dan target regresi
X = df[['semester1', 'semester2', 'semester3', 'semester4']]
y_reg = df['semester5']

# Kategorisasi untuk Naive Bayes
def ip_to_label(ip):
    if ip >= 3.5:
        return "tinggi"
    elif ip >= 2.75:
        return "sedang"
    else:
        return "rendah"

y_class = df['semester5'].apply(ip_to_label)

# Train Linear Regression
reg_model = LinearRegression()
reg_model.fit(X, y_reg)

# Train Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X, y_class)

# Save both models
with open("model_reg.pkl", "wb") as f:
    pickle.dump(reg_model, f)

with open("model_nb.pkl", "wb") as f:
    pickle.dump(nb_model, f)

print("✅ Model regresi dan naive bayes berhasil disimpan.")
