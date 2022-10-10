import pandas as pd
import re


df = pd.read_csv("data/Innovation_and_Pollution_Data.csv", encoding = "ISO-8859-1", engine='python')


# Rows and Columns
print("Rows and Columns: ")
print(df.shape)

# Data non null
print("Number of null: {}".format(df.isnull().sum()))

# Types of values
print(df.info())

# Each row is a country
print(df.Country.value_counts())

# Colnames
colNames = list(df.columns)
print(colNames)

# United States is not in the data base
countries = list(df['Country'].value_counts().index)
print("Countries of variable Country")
print(type(countries))
print(sorted(countries))

def find_the_patter(chain, pattern):
    return bool(re.search(pattern, chain))
print("Return the pattern")
result = [find_the_patter(p, "Mexico") for p in sorted(countries)]
print(any(result))





