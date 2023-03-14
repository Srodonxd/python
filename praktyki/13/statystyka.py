import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# ustalenie nagłówka użytkownika
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# pobieranie danych ze Stack Overflow
response = requests.get("https://insights.stackoverflow.com/survey/2021", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# znajdowanie tabeli z danymi
table = soup.find("table", {"class": "survey-results"})

# inicjalizacja list, w których będą przechowywane dane
languages = []
popularity = []

# przeglądanie wierszy w tabeli i pobieranie danych o językach programowania
for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    language = cells[0].text.strip()
    percentage = cells[1].text.strip()
    description = cells[2].text.strip()
    languages.append(language)
    popularity.append(float(percentage.strip("%")))

# wyświetlenie wykresu popularności języków programowania
plt.bar(languages, popularity)
plt.xticks(rotation=90)
plt.title("Najpopularniejsze języki programowania w 2021 roku")
plt.show()
