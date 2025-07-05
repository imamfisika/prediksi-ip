from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
import os

app = FastAPI()

class IPSemester(BaseModel):
    semester1: float = 0.0
    semester2: float = 0.0
    semester3: float = 0.0
    semester4: float = 0.0

@app.get("/")
def home():
    return {"message": "API prediksi IP aktif."}

@app.post("/predict/{semester}")
def predict_semester(semester: int, data: IPSemester):
    if semester < 2 or semester > 5:
        raise HTTPException(status_code=400, detail="Semester harus antara 2 dan 5.")

    model_path = f"models/model_sem{semester}.pkl"
    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="Model tidak ditemukan.")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Ambil input sesuai fitur yang dibutuhkan
    fitur = [f"semester{i}" for i in range(1, semester)]
    input_data = pd.DataFrame([data.dict()])
    input_df = input_data[fitur]

    pred = model.predict(input_df)[0]
    return {f"prediksi_ip_semester{semester}": round(pred, 2)}

@app.post("/predict/5/kategori")
def predict_kategori(data: IPSemester):
    model_path = "models/model_nb_sem5.pkl"
    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="Model kategori tidak ditemukan.")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    input_df = pd.DataFrame([{
        "semester1": data.semester1,
        "semester2": data.semester2,
        "semester3": data.semester3,
        "semester4": data.semester4,
    }])

    pred = model.predict(input_df)[0]
    return {"kategori_ip_semester5": pred}
