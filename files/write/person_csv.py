from faker import Faker
import csv

# user faker to create 1000 random people data
output = open('data.csv','w')
fake = Faker()
header = ['name','age','street','city','state','zip','lng','lat']
mywriter = csv.writer(output)
mywriter.writerow(header)

for r in range(1000):
    mywriter.writerow([
        fake.name(),
        fake.random_int(min=18, max=80, step=1),
        fake.street_address(),
        fake.city(),
        fake.state(),
        fake.zipcode(),
        fake.longitude(),
        fake.latitude()
    ])
output.close()

# read the .csv file as a dictionary
with open('data.csv') as f:
    myreader = csv.DictReader(f)
    headers = next(myreader)
    for row in myreader:
        print(row['name'])