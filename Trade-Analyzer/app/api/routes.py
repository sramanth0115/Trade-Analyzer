from fastapi import APIRouter
from app.services.analysis import analyze_sector

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze(sector: str):
    return await analyze_sector(sector)
