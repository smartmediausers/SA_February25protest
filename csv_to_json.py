import pandas as pd

df = pd.read_csv(r'messages.csv',delimiter=";")
df.to_json(r'messages.json', orient='index')