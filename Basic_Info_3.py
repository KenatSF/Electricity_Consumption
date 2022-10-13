import pandas as pd
from itertools import compress

df = pd.read_csv("data/powerplants (global) - global_power_plants.csv", encoding = "ISO-8859-1", engine='python')
df = df[df.columns.difference(['country code', 'estimated_generation_gwh_2021', 'other_fuel2', 'other_fuel3', 'secondary fuel', 'geolocation_source'])]

#       ->  0.-
print(df.shape)

#       ->  1.-
print("     Columns names")
columns_names = df.columns.tolist()

#       ->  2.-
print("     Data types")
#print(df.dtypes)

#       -> 3.-
print("     Null data")
print(df.isnull().sum())

#       -> 4.-
print("     Countries exploration")
countries_names = df['country_long'].value_counts().index.tolist()
print("Countries total in the database {}".format(len(countries_names)))

#       -> 5.-  Selecting the countries to study
# We have to make sure that these countries, actually are inside the data-base
from Tool_1_Find_The_Country import Word_Searcher as wsk
searcher = wsk(countries_names)

countries_to_watch = ['Sweden', 'Singapore', 'Switzerland', 'Netherlands', 'Finland',
                      'Algeria', 'Ethiopia', 'Myanmar',
                      'United States of America', 'China', 'Russia']
searcher_booleans = searcher.find_entire_list(countries_to_watch)
countries_names_to_watch = list(compress(countries_to_watch, searcher_booleans))        # -> All countries are loaded
print("     Countries to study inside this new database from the last database:")
print(countries_names_to_watch)


#       -> 6.-
print("     Type of energy exploration")
#fuel_type = df.primary_fuel.value_counts().index.tolist()[0:6]
fuel_type = ['Solar', 'Gas']
print(fuel_type)

#       -> 7.-
print("     Final countries to invest")
countries_to_invest = ['Sweden', 'Singapore', 'Switzerland', 'Netherlands', 'Finland', 'United States of America']




df_clean = df.loc[df['owner of plant'].notnull(), ]

df_clean = df_clean[df_clean['country_long'].isin(countries_to_invest)]
df_clean = df_clean[df_clean['primary_fuel'].isin(fuel_type)]

print(df_clean.country_long.value_counts())
print(df_clean.shape)




