import feedparser

async def search_market(sector: str) -> str:
    """
    Scrape live market news using Google News RSS
    """
    query = f"{sector}"
    rss_url = (
        "https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    )

    feed = feedparser.parse(rss_url)

    if not feed.entries:
        return f"No live news found for {sector} sector."

    news_items = []
    for entry in feed.entries[:5]:  # top 5 news
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        link = entry.get("link", "")
        news_items.append(
            f"- {title}\n  {summary}\n  Source: {link}"
        )

    return "\n\n".join(news_items)
