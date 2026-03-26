from fastapi import APIRouter, Body
from app import state
from app.services.ml_service import train

router=APIRouter()

@router.post("/train")

def train_model(data=Body(...)):

    target=data["target"]

    return train(

    state.CURRENT_DATASET,

    target

    )