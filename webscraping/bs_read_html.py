import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/World_population"

data = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")

tables = soup.find_all('table')

# create DataFrames using read_html
population_data_read_html = pd.read_html(str(tables[5]), flavor = 'bs4')[0]

# use read_html to directly get DataFrames from a url
dataframe_list = pd.read_html(url, flavor = 'bs4')

# there are 25 DataFrames just like using find_all()
print(len(dataframe_list))

# pick the DataFrame from the list
population_data_table = dataframe_list[5]

# use match parameter to select the table
population_data_table = pd.read_html(url, match = "10 most densely populated countries", flavor = 'bs4')[0]
