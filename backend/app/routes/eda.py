from fastapi import APIRouter
from app import state

router=APIRouter()

@router.get("/eda")

def eda():

    df=state.CURRENT_DATASET

    return {

    "shape":df.shape,

    "columns":list(df.columns)

    }