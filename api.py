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
    semester5: float = 0.0
    semester6: float = 0.0
    semester7: float = 0.0

@app.get("/")
def home():
    return {"message": "API prediksi IP aktif."}

# endporint untuk memprediksi IP semester tertentu
@app.post("/predict/{semester}")
def predict_semester(semester: int, data: IPSemester):
    if semester < 2 or semester > 8:
        raise HTTPException(status_code=400, detail="Semester harus antara 2 dan 8.")

    model_path = f"models/model_sem{semester}.pkl"
    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="Model tidak ditemukan.")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    fitur = [f"semester{i}" for i in range(1, semester)]
    input_df = pd.DataFrame([data.dict()])[fitur]

    pred = model.predict(input_df)[0]
    return {f"prediksi_ip_semester{semester}": round(pred, 2)}

# endpoint untuk memprediksi kategori IP semester tertentu
@app.post("/predict/{semester}/kategori")
def predict_kategori(semester: int, data: IPSemester):
    if semester < 2 or semester > 8:
        raise HTTPException(status_code=400, detail="Semester harus antara 2 dan 8.")

    path = f"models/nb_model_sem{semester}.pkl"
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Model kategori tidak ditemukan.")

    with open(path, "rb") as f:
        model = pickle.load(f)

    fitur = [f"semester{i}" for i in range(1, semester)]
    input_df = pd.DataFrame([data.dict()])[fitur]

    kategori = model.predict(input_df)[0]
    return {f"kategori_ip_semester{semester}": kategori}