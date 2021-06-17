from faker import Faker
import json
import pandas.io.json as pd_JSON

# output = open('data.json','w')
# fake = Faker()
# alldata = {}
# alldata['records'] = []

# for x in range(1000):
#     data = {
#         "name":fake.name(),
#         "age":fake.random_int(min=18, max=80, step=1),
#         "street":fake.street_address(),
#         "city":fake.city(),
#         "state":fake.state(),
#         "zip":fake.zipcode(),
#         "lng":float(fake.longitude()),
#         "lat":float(fake.latitude())
#         }
#     alldata['records'].append(data)

# json.dump(alldata, output)

# with open("data.json","r") as f:
#     data = json.load(f)

# print(type(data))
# print(data['records'][0]['name'])

f = open('data.json','r')
data = pd_JSON.loads(f.read())
df = pd_JSON.json_normalize(data, record_path='records')
print(df.head())

# save as json without flattening
df.to_JSON(orient='records')