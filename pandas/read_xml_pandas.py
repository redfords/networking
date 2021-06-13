import pandas as pd
import xml.etree.ElementTree as etree

# read xml files
tree = etree.parse("fileExample.xml")
root = tree.getroot()
columns = ['Name', 'Phone Number', 'Birthday']
df = pd.DataFrame(columns = columns)

# create a loop to go through the document to append the data to a DataFrame
for node in root:
    name = node.find("name").text
    phonenumber = node.find("phonenumber").text
    birthday = node.find("birthday").text

df = df.append(pd.Series([name, phonenumber, birthday], index = columns), ignore_index = True)

# read XML
tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]

datatframe = pd.DataFrame(columns = columns)

for node in root:
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text 
    title = node.find("title").text 
    division = node.find("division").text 
    building = node.find("building").text
    room = node.find("room").text
    datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room],
    index = columns), ignore_index = True)

# save file
save_file = datatframe.to_csv("employee.csv", index = False)