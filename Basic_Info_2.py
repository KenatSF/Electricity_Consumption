import pandas as pd
import re
from itertools import compress

df = pd.read_csv("data/World Energy Consumption.csv", encoding = "ISO-8859-1", engine='python')


#       Rows and Columns
print("Rows and Columns: ")
print(df.shape)


#       Data get columns with null data
print("Number of null: ")

columns_names = df.columns.tolist()
null_columns = []
for i in range(df.shape[1]):
    if(df.iloc[:, i].isnull().values.any()):
        print("Column: ", columns_names[i], "; Missing values: ", df.iloc[:, i].isnull().sum(), "; Data type: ", df.iloc[:, i].dtypes)
        null_columns.append(columns_names[i])

print(" Columns with null")
print(len(null_columns))
print(null_columns)

print(" Columns with no null")
no_null_columns = list(set(columns_names) - set(null_columns))
#print(no_null_columns)

#       Exploring year column     -> 1900 init year; 2020 end year; Different years: 2020 only 69 obs
print(df.year.describe())
print(df.year.apply(str).value_counts())

#       Exploring country column  -> 242 countries
countries_names = df.country.value_counts().index.tolist()      # -> Global variable
print(df.country.value_counts())

#       Making sure that these specific countries to study are actually in this data base
specific_countries_names = ['Sweden', 'Singapore', 'Czech Republic', 'Hong Kong', 'Norway', 'United Kingdom',
                            'Canada', 'France', 'Iceland', 'Ireland', 'Belgium', 'Austria', 'China', 'Germany',
                            'Denmark', 'Japan', 'Luxembourg', 'Israel', 'Finland', 'Netherlands', 'Switzerland',
                            'Australia']
def find_the_patter(chain, pattern):
    return bool(re.search(pattern, chain))

def find_inside_list(word_to_seek):
    result = [find_the_patter(p, word_to_seek) for p in sorted(countries_names)]
    value = any(result)
    #print("Country: {} is: {}".format(word_to_seek, value))
    return value


trues_variables = list(map(find_inside_list, specific_countries_names))

new_specific_countries_names = list(compress(specific_countries_names, trues_variables))
print("Comparing length:")
print(len(specific_countries_names))
print(len(trues_variables))
print(len(new_specific_countries_names))

print("Countries to study inside this new database from the last database:")
print(new_specific_countries_names)


print(df.primary_energy_consumption.describe())




