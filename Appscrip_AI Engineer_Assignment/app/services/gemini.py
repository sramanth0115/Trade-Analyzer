import os
import httpx

GEMINI_API_KEY = "AIzaSyC5nG6rXlSr7tr2QgNf4XJPvZVaTL9bHs0"

async def generate_analysis(sector: str, data: str) -> str:
    if not GEMINI_API_KEY:
        return "Gemini API key not configured."

    prompt = f"""
You are a market analyst.

Analyze the following information about the Indian {sector} sector
and generate a structured markdown report with:

- Market Overview
- Trade Opportunities
- Risks
- Future Outlook

Information:
{data}
"""

    url = (
    "https://generativelanguage.googleapis.com/v1beta/"
    f"models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
)


    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(url, json=payload)

    if response.status_code != 200:
        return f"Gemini API error: {response.text}"

    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return "Gemini returned an unexpected response format."
