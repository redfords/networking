""" Data analysis

This dataset is from the National Institute of Diabetes and Digestive and Kidney Diseases.

The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based
on certain diagnostic measurements included in the dataset. Several constraints were placed on the
selection of these instances from a larger database. In particular, all patients here are females at
least 21 years old of Pima Indian heritage.

The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor
variables includes the number of pregnancies the patient has had, their BMI, insulin level, age.

We have 768 rows and 9 columns. The first 8 columns represent the features and the last column
represents the target/label. """

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

print("The first 5 rows of the dataframe") 
print(df.head(5))

# view the dimensions of the DataSet
print("Dimensions", df.shape)

# information including the index dtype and columns, non-null values and memory usage
print("DataSet information", df.info())

# view basic statistical details like percentile, mean, std etc. of a DataFrame
print("Basic statistical details", df.describe())

""" Identify and handle missing values
There are two methods to detect missing data:
.isnull()
.notnull()

The output is a boolean value indicating whether the value that is passed into the argument is in fact
missing data. """

missing_data = df.isnull()
print(missing_data.head(5))

""" Count missing values in each column
Using a for loop in Python, we can quickly figure out the number of missing values in each column.
"True" represents a missing value, "False" means the value is present in the dataset. In the body of
the for loop the method ".value_counts()" counts the number of "True" values. """

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

""" Correct data format
Check all data is in the correct format (int, float, text or other). In Pandas, we use:
.dtype() to check the data type
.astype() to change the data type

Numerical variables should have type 'float' or 'int' """

print(df.dtypes)

""" Visualization
Use Seaborn and Matplotlib as visualization libraries. As you can see 65.10% females are Diabetic and
34.90% are Not Diabetic.
"""

labels = 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()
