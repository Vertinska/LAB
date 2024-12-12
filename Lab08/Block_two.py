import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://worldathletics.org/records/toplists"
DISCIPLINES = {
    "high-jump": "jumps/high-jump",
    "pole-vault": "jumps/pole-vault",
    "long-jump": "jumps/long-jump",
    "triple-jump": "jumps/triple-jump"
}
GENDERS = ["men", "women"]
YEARS = range(2024, 2025)
OUTPUT_FILE = "top_results.csv"


def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def parse_results(soup):
    table = soup.find("table", class_="records-table")
    if not table:
        return None

    row = table.find("tbody").find("tr")
    if not row:
        return None

    cols = row.find_all("td")
   
    return {
        "Competitor": cols[3].text.strip(),
        "Nat": cols[5].text.strip(),
        "Mark": cols[1].text.strip(),
        "Date": cols[9].text.strip()
    }

def scrape_top_results():
    results = []

    for discipline, path in DISCIPLINES.items():
        for gender in GENDERS:
            for year in YEARS:
                url = f"{BASE_URL}/{path}/all/{gender}/senior/{year}"
                print(f"Загружается: {url}")

                try:
                    soup = fetch_page(url)
                    top_result = parse_results(soup)

                    if top_result:
                        top_result.update({
                            "Year": year,
                            "Competitor": top_result["Competitor"],
                            "Nat": top_result["Nat"],
                            "Mark": top_result["Mark"],
                            "Date": top_result["Date"],
                            "Discipline": discipline,
                            "Gender": "Men" if gender == "men" else "Women"
                        })
                        results.append(top_result)

                except Exception as e:
                    print(f"Ошибка при обработке {url}: {e}")

    return results


def save_to_csv(data, file_path):
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Year", "Discipline", "Gender", "Competitor", "Nat", "Mark", "Date"])
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    try:
        top_results = scrape_top_results()
        save_to_csv(top_results, OUTPUT_FILE)
        print(f"Данные сохранены в файл: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
