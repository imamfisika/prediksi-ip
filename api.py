from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

# Load model
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    raise Exception("Model belum dilatih. Jalankan train_model.py terlebih dahulu.")

# Definisikan API
app = FastAPI()

# Definisikan schema input
class IPSemester(BaseModel):
    semester1: float
    semester2: float
    semester3: float
    semester4: float

@app.get("/")
def root():
    return {"message": "API prediksi IP siap digunakan."}

@app.post("/predict")
def predict_ip(data: IPSemester):
    try:
        input_df = pd.DataFrame([data.dict()])
        prediction = model.predict(input_df)[0]
        return {"prediksi_ip_semester5": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
