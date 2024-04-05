import json
import requests
import pprint
import base64

url = 'https://api.gotit.ai/NLU/v1.5/Analyze'

data = {
    "T": "Não tenho disponibilidade de horário pois tenho filhos pequenos e isso dificulta meu acesso aos estudos",
    "S": True,
    "EM": True
}

#data = {'T': 'Jonas Schettini  CHORA PETEZADA ALOPRADA, VCS NÃO TEM ISSO, CHORA DE INVEJA KKKKKK KKKKKK', 'S': True, 'EM': True}

data_json = json.dumps(data)

userAndPass = base64.b64encode(b"sua_chave_para_processamento").decode("ascii")

headers = {'Content-type': 'application/json', "Authorization": "Basic %s" %  userAndPass}

response = requests.post(url, data=data_json, headers=headers)

pprint.pprint(response.json())
pprint.pprint(response.status_code)