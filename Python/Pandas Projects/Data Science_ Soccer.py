import pandas as pd 

all_tables = pd.read_html('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')
print(all_tables[18])
