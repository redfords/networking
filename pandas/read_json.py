import pandas as pd
import json

# read json
with open('filesample.json', 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

""" Serialization using dump() function
json.dump() method can be used for writing to JSON file.
Parameters:
dictionary – name of dictionary which should be converted to JSON object.
file pointer – pointer of the file opened in write or append mode.
"""

with open('person.json', 'w') as f:
    json.dump(person, f)

""" Serialization using dumps() function
json.dumps() that helps in converting a dictionary to a JSON object.
Parameters:
dictionary – name of dictionary which should be converted to JSON object.
indent – defines the number of units for indentation
"""

json_object = json.dumps(person, indent = 4) 
  
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

""" Deserialization
The json.load() function loads the json content from a json file into a dictionary.
Parameter:
file pointer – a file pointer that points to a JSON file.
"""

with open('sample.json', 'r') as openfile: 
    json_object = json.load(openfile) 
  
print(json_object) 
print(type(json_object))