from app.services.search import search_market
from app.services.gemini import generate_analysis

async def analyze_sector(sector: str):
    data = await search_market(sector)
    report = await generate_analysis(sector, data)
    report = report + "##"
    report = report.replace("\n", "").replace(".-", ".")
    result = []
    start = 0
    for n in range(len(report)-1):
        if report[n] == '#' and report[n+1] == '#':
            result.append(report[start:n])
            start = n
    result = result[1:]
    print(report)
    return {"sector": sector, "report_markdown": result}