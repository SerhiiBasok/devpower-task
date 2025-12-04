# Data Scraper & DB Loader

This project collects data about countries and regions from different sources (Wikipedia or Statisticstimes) and saves it into a PostgreSQL database.

---

## Quick Start

1. **Clone the repository**

Use Git to clone the repository and enter the folder:

```bash
git clone https://github.com/SerhiiBasok/devpower-task.git
```

```bash
cd devpower-task
```


2. **Create a `.env` file**

Copy the example `.env.sample` to `.env`:


> You can change `Wicipedia` or `Statisticstimes` to scrape data

3. **Run Docker containers**

- To load data into the database:
```bash
docker-compose up get_data
```

- To print data from the database:


```bash
docker-compose up print_data
```

> Both commands automatically use the settings from the `.env` file.

---

## Notes

- The parser is selected through the `PARSER` variable in `.env`. Available options:  
  - `wiki_parser` — Wikipedia  
  - `stat_parser` — Statisticstimes

---
