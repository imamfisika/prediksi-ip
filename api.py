from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

with open("model_reg.pkl", "rb") as f:
    reg_model = pickle.load(f)

with open("model_nb.pkl", "rb") as f:
    nb_model = pickle.load(f)

class IPSemester(BaseModel):
    semester1: float
    semester2: float
    semester3: float
    semester4: float

@app.get("/")
def home():
    return {"message": "API prediksi IP aktif."}

@app.post("/predict")
def predict_all(data: IPSemester):
    df = pd.DataFrame([data.dict()])
    nilai = reg_model.predict(df)[0]
    kategori = nb_model.predict(df)[0]
    return {
        "prediksi_ip_semester5": round(nilai, 2),
        "kategori_ip_semester5": kategori
    }
