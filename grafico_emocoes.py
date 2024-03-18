import pandas as pd
import matplotlib.pyplot as plt
import json

# Carregando os dados do JSON
with open('agrupados_bolsonaro.json', 'r') as file:
    data = json.load(file)

# Transformando os dados em DataFrame
timestamps = list(data.keys())
emotions = [data[ts]['emotions'] for ts in timestamps]

df_emotions = pd.DataFrame(emotions, index=timestamps)

# Gerando o gráfico
plt.figure(figsize=(14, 7))
for emotion in df_emotions.columns:
    plt.plot(df_emotions.index, df_emotions[emotion], label=emotion)

plt.title('Emoções ao Longo do Tempo - Bolsonaro')
plt.xlabel('Timestamp')
plt.ylabel('Valor das Emoções')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()