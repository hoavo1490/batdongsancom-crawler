import pandas as pd
df = pd.read_csv('list.csv')
# any operations on dataframe df
df.to_json('file.json')