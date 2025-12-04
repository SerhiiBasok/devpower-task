import os

from dotenv import load_dotenv

from app.parsers.parser import Parser

load_dotenv()

# Parser settings for statisticstimes
stat_parser = Parser(
    url=os.getenv("STAT_URL"),
    table_selector={"id": "table_id"},
    population_index=1,
    region_index=-1,
)

# Parser settings for Wikipedia
wiki_parser = Parser(
    url=os.getenv("WIKI_URL"),
    table_selector={"class_": "wikitable"},
    population_index=2,
    region_index=4,
)

parsers = {
    "stat_parser": stat_parser,
    "wiki_parser": wiki_parser,
}

parser_name = os.getenv("PARSER")
