import pandas as pd
import numpy as np

# read csv files
file = "FileExample.csv"
df = pd.read_csv(file)
df.columns = ['Name', 'Phone Number', 'Birthday']

# read csv from url
url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url)
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

# select multiple columns
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]

# select rows using .iloc and .loc
first_row = df.loc[0]
rows_first_name = df.loc[[0,1,2], "First Name" ]

# select the 0th,1st and 2nd row of "First Name" column only
rows_first_name = df.iloc[[0, 1, 2], 0]

""" Transform Function in Pandas
Python’s Transform function returns a self-produced dataframe with transformed values after applying
the function specified in its parameter. """

# create a DataFrame
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns = ['a', 'b', 'c'])

# add 10 to each element
df = df.transform(func = lambda x : x + 10)

# find the square root of each element
result = df.transform(func = ['sqrt'])
