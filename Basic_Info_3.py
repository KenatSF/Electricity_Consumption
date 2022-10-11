import pandas as pd


df = pd.read_csv("data/powerplants (global) - global_power_plants.csv", encoding = "ISO-8859-1", engine='python')
df = df[df.columns.difference(['country code', 'estimated_generation_gwh_2021', 'other_fuel2', 'other_fuel3', 'secondary fuel', 'geolocation_source'])]

#       ->  0.-
print(df.shape)

#       ->  1.-
print("Columns names")
columns_names = df.columns.tolist()

#       ->  2.-
print("Data types")
#print(df.dtypes)

#       -> 3.-
print("Null data")
print(df.isnull().sum())

#       -> 4.-
print("Countries exploration")
countries_names = df['country_long'].value_counts().index.tolist()
print(len(countries_names))
print(countries_names)

from Tool_1_Find_The_Country import Word_Searcher as wsk
searcher = wsk(countries_names)
print("Find a specific country inside the countries")
print(searcher.find_inside_list("Myanmar"))

#print(df['primary_fuel'].value_counts())


