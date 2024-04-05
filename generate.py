import pandas as pd
import matplotlib.pyplot as plt
import json

# Assuming the JSON data is saved in a file named 'messages.json' in the '/mnt/data/' directory.
file_path = 'messages.json'
df_list = []

with open(file_path, 'r') as arquivo:
    data = json.load(arquivo)



for key, value in data.items():
    
    emotions = value['emotions']
    emotions['sentiment_score'] = value['sentiment']['score']
    df_list.append(pd.DataFrame(emotions, index=[key]))


#df = pd.concat(df_list)
df = pd.concat(df_list, ignore_index=True)

# Calculando a média de cada coluna
#mean_values = df.mean()

# Calculando a média de cada coluna
std_values = df.std()

'''
# Plotando os valores médios
plt.figure(figsize=(10, 6))
mean_values.plot(kind='bar')
plt.title('Average Emotions and Sentiment Score')
plt.xlabel('Category')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
'''


# Plotando o desvio padrão
plt.figure(figsize=(10, 6))
std_values.plot(kind='bar')
plt.title('Standard Deviation Emotions and Sentiment Score')
plt.xlabel('Category')
plt.ylabel('Std Score')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

'''
# Plotando os dados
plt.figure(figsize=(10, 6))
for column in df.columns:
    plt.plot(df.index, df[column], marker='o', label=column)

plt.title('Emotions Over Messages')
plt.xlabel('Message Index')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.show()

'''

