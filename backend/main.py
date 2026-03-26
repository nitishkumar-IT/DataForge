from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router as upload_router
from app.routes.clean import router as clean_router
from app.routes.eda import router as eda_router
from app.routes.ml import router as ml_router
from app.routes.predict import router as predict_router

app=FastAPI()

app.add_middleware(

CORSMiddleware,

allow_origins=["*"],

allow_methods=["*"],

allow_headers=["*"]

)

app.include_router(upload_router)
app.include_router(clean_router)
app.include_router(eda_router)
app.include_router(ml_router)
app.include_router(predict_router)

@app.get("/")

def home():

    return {"message":"DataForge API running"}