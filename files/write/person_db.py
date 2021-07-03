import psycopg2 as db
import sys
from faker import Faker

connection = None

try:

    connection = db.connect(
        host="localhost",
        port=5433,
        database="test",
        user="postgres",
        password="password"
        )

    # create fake data
    fake = Faker()
    data = []
    i = 1

    for r in range(1000):
        data.append((i, fake.name(), fake.street_address(), fake.city(), fake.zipcode()))
        i += 1

    data_for_db = tuple(data)

    # load into db
    cursor = connection.cursor()
    query = "insert into users (id, name, street, city, zip) values (%s, %s, %s, %s, %s)"
    cursor.executemany(query,data_for_db)
    connection.commit()
    
    # fetchall
    query = "select * from users limit 10"
    cursor.execute(query)
    records = cursor.fetchall()

    for row in records:
        print("Id = ", row[0])
        print("Name = ", row[1])
        print("Street = ", row[2])
        print("City = ", row[3])
        print("Zip = ", row[4], '\n')

    # fetchone
    query = "select count(*) from users"
    cursor.execute(query)
    result = cursor.fetchone()[0]

    print("total count", result)

except db.DatabaseError as e:

    print(f"Error {e}")
    sys.exit(1)

finally:

    if connection:
        connection.close()
