import requests
from bs4 import BeautifulSoup

html = "<table><tr><td>Pizza Place</td><td>Orders</td><td>Slices</td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144</td></table>"

table = BeautifulSoup(html, 'html5lib')

print(table.prettify())

table_row = table.find_all(name = 'tr')

first_row = table_row[0]
print(first_row)
# <tr><td>Pizza Place</td><td>Orders</td><td>Slices</td></tr>

print(first_row.td)
# <td>Pizza Place</td>

for i, row in enumerate(table_row):
    print("row", i)
    cells = row.find_all("td")

    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)

""" Flight Table
%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>
"""

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')

table_rows=table_bs.find_all('tr')
print(table_rows)

first_row =table_rows[0]
print(first_row)

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('colunm', j, "cell", cell)

list_input = table_bs.find_all(name = ["tr", "td"])

""" Filter by attributes """

table_flight= table_bs.find_all(id = "flight")

# find elements that have links to the FLorida Wikipedia page
list_input = table_bs.find_all(href = "https://en.wikipedia.org/wiki/Florida")

# find all tags with href value
list_href = table_bs.find_all(href = True)

# search for strings instead of tags
list_string = table_bs.find_all(string = "Florida")

