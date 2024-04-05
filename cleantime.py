import json
from datetime import datetime

arquivo_entrada = 'messages.json'

# Supondo que o JSON esteja salvo em uma string para fins de demonstração
with open(arquivo_entrada, 'r') as arquivo:
    data = json.load(arquivo)


for key, value in data.items():
    #print(str(value['timestamp']).replace("  PM", " PM"))
    value['timestamp'] = "0" + (str(value['timestamp']).replace("  PM", ""))
    
# Salvar o dicionário atualizado de volta em um arquivo JSON
with open('mensagem_atualizada.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)