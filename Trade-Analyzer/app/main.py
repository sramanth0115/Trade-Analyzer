from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Trade Opportunities API")

app.include_router(router)