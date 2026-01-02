import feedparser
import html
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

async def search_market(sector: str) -> str:
    query = quote_plus(sector)

    rss_url = (
        f"https://news.google.com/rss/search?q={query}"
        "&hl=en-IN&gl=IN&ceid=IN:en"
    )

    feed = feedparser.parse(rss_url)

    if not feed.entries:
        return f"No live news found for {sector} sector."

    news_items = []

    for entry in feed.entries[:5]:
        title = entry.get("title", "No title")

        # Clean HTML summary properly
        raw_summary = entry.get("summary", "")
        raw_summary = html.unescape(raw_summary)
        soup = BeautifulSoup(raw_summary, "html.parser")
        clean_summary = soup.get_text(" ", strip=True)

        link = entry.get("link", "")
        source = entry.get("source", {}).get("title", "Unknown source")

        news_items.append(
            f"  Title: {title}\n"
            f"  Source: {source}\n"
            f"  Summary: {clean_summary}\n"
        )
    return "\n\n".join(news_items)
