from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_user
from app.services.analysis import analyze_sector

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze(sector: str, user: str = Depends(get_current_user)):
    return await analyze_sector(sector)