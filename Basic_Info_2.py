import pandas as pd
import re
from itertools import compress
from Tool_1_Find_The_Country import Word_Searcher as wsk

df = pd.read_csv("data/World Energy Consumption.csv", encoding = "ISO-8859-1", engine='python')


#       Rows and Columns
print("Rows and Columns: ")
print(df.shape)

#       Data get columns with null data
print("Number of null: ")


#       Get rid of a useless column
df = df[df.columns.difference(['iso_code'])]


#       Columns names
columns_names = df.columns.tolist()


#       Columns with null data
null_columns = []
for i in range(df.shape[1]):
    if(df.iloc[:, i].isnull().values.any()):
        print("Column: ", columns_names[i], "; Missing values: ", df.iloc[:, i].isnull().sum(), "; Data type: ", df.iloc[:, i].dtypes)
        null_columns.append(columns_names[i])

print(" Columns with null rows")
print("Length: {}".format(len(null_columns)))
print(null_columns)

print(" Columns name with no null rows")
no_null_columns = list(set(columns_names) - set(null_columns))
print(no_null_columns)


#       Exploring year column     -> 1900 init year; 2020 end year; Different years: 2020 only 69 obs
print("Exploring year column  \n")
print(df.year.describe())
print(df.year.apply(str).value_counts())


#       Exploring country column  -> 242 countries
print("Exploring country column \n")
countries_names = df.country.value_counts().index.tolist()      # -> Global variable
print(df.country.value_counts())


#       Selecting the countries to study
# We have to make sure that these countries, actually are inside the data-base
# Note: In the last data base USA wasn't inside, but here, this country it does inside this data-base
specific_countries_names = ['Sweden', 'Singapore', 'Switzerland', 'Netherlands', 'Finland',
                            'Algeria', 'Ethiopia', 'Myanmar',
                            'United States', 'Russia', 'China']


searcher = wsk(countries_names)
searcher_booleans = searcher.find_entire_list(specific_countries_names)
new_specific_countries_names = list(compress(specific_countries_names, searcher_booleans))
print("Countries to study inside this new database from the last database:")
print(new_specific_countries_names)


#       Find a if there is a specific country
#print("Find a if there is a specific country")
#print(searcher.find_inside_list("United States"))


