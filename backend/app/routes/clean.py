from fastapi import APIRouter
from app import state

router = APIRouter()

@router.post("/clean")

def clean():

    df = state.CURRENT_DATASET

    df = df.drop_duplicates()

    state.CURRENT_DATASET=df

    return {"status":"cleaned"}