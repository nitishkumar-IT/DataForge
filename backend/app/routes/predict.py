from fastapi import APIRouter, Body
import joblib

router=APIRouter()

model=None

try:

    model=joblib.load("models/model.pkl")

except:

    model=None

@router.post("/predict")

def predict(data=Body(...)):

    if model is None:

        return {"error":"model not trained"}

    result=model.predict([data["data"]])

    return {

    "prediction":

    float(result[0])

    }