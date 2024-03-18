import pandas as pd
import matplotlib.pyplot as plt
import json

# Carregando os dados do JSON
with open('agrupados_todos.json', 'r') as file:
    data = json.load(file)

# Transformando os dados em DataFrame
timestamps = list(data.keys())
sentiment = [data[ts]['sentiment'] for ts in timestamps]

df_sentiment = pd.DataFrame(sentiment, index=timestamps)

# Gerando o gráfico
plt.figure(figsize=(14, 7))
for s in df_sentiment.columns:
    plt.plot(df_sentiment.index, df_sentiment[s], label=s)

plt.title('Sentimento acumulado ao Longo do Tempo')
plt.xlabel('Timestamp')
plt.ylabel('Pontuação acumulada do sentimento')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()