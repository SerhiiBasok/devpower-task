import httpx
from bs4 import BeautifulSoup
from typing import Dict


class Parser:

    def __init__(
        self,
        url: str,
        table_selector: Dict[str, str],
        population_index: int,
        region_index: int,
    ):
        self.url = url
        self.table_selector = table_selector
        self.population_index = population_index
        self.region_index = region_index

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
        table = soup.find(**self.table_selector)

        rows = table.find_all("tr")[1:]

        result = []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 5:
                continue

            if cols[0].get_text(strip=True) == "World":
                continue

            country_name = cols[0].get_text(strip=True)
            population_text = (
                cols[self.population_index].get_text(strip=True).replace(",", "")
            )
            region_name = cols[self.region_index].get_text(strip=True)

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
