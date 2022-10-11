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

columns_names = df.columns.tolist()
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

#    Making sure that these specific countries to study are actually in this data base. Note:There was a change of plans
old_specific_countries_names = ['Sweden', 'Singapore', 'Czech Republic', 'Hong Kong', 'Norway', 'United Kingdom',
                            'Canada', 'France', 'Iceland', 'Ireland', 'Belgium', 'Austria', 'China', 'Germany',
                            'Denmark', 'Japan', 'Luxembourg', 'Israel', 'Finland', 'Netherlands', 'Switzerland',
                            'Australia']

print("Countries to study inside this new database from the last database:")
searcher = wsk(countries_names)
searcher_booleans = searcher.find_entire_list(old_specific_countries_names)
new_new_specific_countries_names = list(compress(old_specific_countries_names, searcher_booleans))
print(new_new_specific_countries_names)


#       Find a if there is a specific country
#print("Find a if there is a specific country")
#print(searcher.find_inside_list("United States"))



# In function of the countries found in the last data base, we are gonna focus on those ones
# Note: In the last data base USA wasn't inside, but here this countries it does inside this one
specific_countries_names = ['Sweden', 'Singapore', 'Switzerland', 'Netherlands', 'Finland',
                            'United States', 'Russia', 'China']
print("Final Countries to study inside this new database from the last database:")
print(specific_countries_names)

print(df.year.dtypes)

print(df.primary_energy_consumption.describe())




