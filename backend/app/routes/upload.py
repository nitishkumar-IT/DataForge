from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app import state

router = APIRouter()

@router.post("/upload")

async def upload(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    state.CURRENT_DATASET = df

    return {"rows":len(df)}