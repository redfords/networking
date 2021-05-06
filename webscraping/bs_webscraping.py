import requests
from bs4 import BeautifulSoup

url = "http://www.ibm.com"

data  = requests.get(url).text

# create a BeautifulSoup object using the variable data
soup = BeautifulSoup(data, "html5lib")

# scrape all links
for link in soup.find_all('a', href = True):  # a link is represented by the tag <a>
    print(link.get('href'))

# scape all images
for link in soup.find_all('img'): # an image is represented by the tag <img>
    print(link)
    print(link.get('src'))

# scrape data from HTML tables
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data  = requests.get(url).text

soup = BeautifulSoup(data,"html5lib")

# find a html table in the web page
table = soup.find('table') # a table is represented by the tag <table>

# get all rows from the table
for row in table.find_all('tr'): # a table row is represented by the tag <tr>
    # get all columns in each row.
    cols = row.find_all('td') # a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
