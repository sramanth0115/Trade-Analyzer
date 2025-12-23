from app.services.search import search_market
from app.services.gemini import generate_analysis

async def analyze_sector(sector: str):
    data = await search_market(sector)
    report = await generate_analysis(sector, data)
    return {"sector": sector, "report_markdown": report}