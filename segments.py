import json
from datetime import datetime

arquivo_entrada = 'segmentado.json'
interval_dict = {}
palavra = 'bolsonaro'

# Supondo que o JSON esteja salvo em uma string para fins de demonstração
with open(arquivo_entrada, 'r') as arquivo:
    data = json.load(arquivo)


for key, value in data.items():
    if (value['time_interval'] not in interval_dict) and (palavra in value["message"].lower()):
        interval_dict[value['time_interval']] = {
            "emotions": {
            "sadness": value["emotions"]["sadness"],
            "joy": value["emotions"]["joy"],
            "fear": value["emotions"]["fear"],
            "disgust": value["emotions"]["disgust"],
            "anger": value["emotions"]["disgust"]
        },
        "sentiment": {
            "score": value["sentiment"]["score"],
        },
        "elements": 0.0}
    elif (value['time_interval'] in interval_dict) and (palavra in value["message"].lower()):
        interval_dict[value['time_interval']] = {
            "emotions": {
            "sadness": interval_dict[value['time_interval']]["emotions"]["sadness"]+value["emotions"]["sadness"],
            "joy": interval_dict[value['time_interval']]["emotions"]["joy"]+value["emotions"]["joy"],
            "fear": interval_dict[value['time_interval']]["emotions"]["fear"]+value["emotions"]["fear"],
            "disgust": interval_dict[value['time_interval']]["emotions"]["disgust"]+value["emotions"]["disgust"],
            "anger": interval_dict[value['time_interval']]["emotions"]["anger"]+value["emotions"]["anger"]
        },
        "sentiment": {
            "score": interval_dict[value['time_interval']]["sentiment"]["score"]+value["sentiment"]["score"],
        },
        "elements": interval_dict[value['time_interval']]['elements'] + 1.0}


for key, value in interval_dict.items():
    value["emotions"]["sadness"] = value["emotions"]["sadness"]/value["elements"]
    value["emotions"]["joy"] = value["emotions"]["joy"]/value["elements"]
    value["emotions"]["fear"] = value["emotions"]["fear"]/value["elements"]
    value["emotions"]["disgust"] = value["emotions"]["disgust"]/value["elements"]
    value["emotions"]["anger"] = value["emotions"]["anger"]/value["elements"]
    



    
# Salvar o dicionário atualizado de volta em um arquivo JSON
with open('agrupados_bolsonaro.json', 'w') as json_file:
    json.dump(interval_dict, json_file, indent=4)