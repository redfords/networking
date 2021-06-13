import xml.etree.ElementTree as et

# create the file structure
employee = et.Element('employee')
details = et.SubElement(employee, 'details')
first = et.SubElement(details, 'firstname')
second = et.SubElement(details, 'lastname')
third = et.SubElement(details, 'age')
first.text = 'joana'
second.text = 'piovaroli'
third.text = '23'

# create a new XML file with the results
mydata1 = et.ElementTree(employee)

# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

