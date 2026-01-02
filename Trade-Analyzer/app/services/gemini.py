import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def generate_analysis(sector: str, data: str) -> str:
    if not GEMINI_API_KEY:
        return "Gemini API key not configured."

    prompt = f"""
You are a market analyst.

Analyze the Indian {sector} sector using ONLY relevant technology-related information.
Ignore unrelated meanings of the term.

Generate a **clear, point-wise markdown report** using bullet points.

Use this exact structure:

## Market Overview
- Point 1
- Point 2
- Point 3

## Trade Opportunities
- Point 1
- Point 2

## Risks
- Point 1
- Point 2

## Future Outlook
- Point 1
- Point 2

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
