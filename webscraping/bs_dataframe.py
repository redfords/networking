import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/World_population"

data  = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")

tables = soup.find_all('table')

# check how many tables were found
print(len(tables))

# find the 10 most populated countries table
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index

print(table_index)

# print(tables[table_index].prettify())

population_data = pd.DataFrame()

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index = True)

print(population_data)