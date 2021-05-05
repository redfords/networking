import requests
from bs4 import BeautifulSoup

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000,000 </p><h3> Kevin Durant </h3><p> Salary: $73,200,000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

print(soup)

""" BeautifulSoup objects """

tag_object = soup.title
print(tag_object)
# <title>Page Title</title>

tag_object = soup.h3
print(tag_object)
# <h3><b id="boldest">Lebron James</b></h3>

tag_child = tag_object.b
print(tag_child)
# <b id="boldest">Lebron James</b>

parent_tag = tag_child.parent
print(parent_tag)
# <h3><b id="boldest">Lebron James</b></h3>

sibling_1 = tag_object.next_sibling
print(sibling_1)
# <p> Salary: $92,000,000 </p>

sibling_2 = sibling_1.next_sibling

print(tag_child.attrs)
print(tag_child.string)

""" Filter find_all """

html = "<table><tr><td>Pizza Place</td><td>Orders</td><td>Slices</td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144</td></table>"

table = BeautifulSoup(html, 'html5lib')

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
