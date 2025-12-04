import httpx
from bs4 import BeautifulSoup

WIKI_URL = (
    "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
)


class WikiParser:
    def __init__(self, url: str = WIKI_URL):
        self.url = url

    async def fetch_html(self) -> str:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        async with httpx.AsyncClient(timeout=30, headers=headers) as client:
            response = await client.get(self.url)
            response.raise_for_status()
            return response.text

    async def parse(self) -> list[dict]:
        html = await self.fetch_html()
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="wikitable")

        rows = table.find_all("tr")[1:]

        result = []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 5:
                continue

            if cols[0].get_text(strip=True) == "World":
                continue

            country_name = cols[0].get_text(strip=True)
            population_text = cols[2].get_text(strip=True).replace(",", "")
            region_name = cols[4].get_text(strip=True)

            if not population_text.isdigit():
                continue

            result.append(
                {
                    "country": country_name,
                    "population": int(population_text),
                    "region": region_name,
                }
            )

        return result
