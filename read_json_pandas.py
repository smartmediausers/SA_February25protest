import json
import requests
import base64

arquivo_entrada = 'messages.json'

# Supondo que o JSON esteja salvo em uma string para fins de demonstração
with open(arquivo_entrada, 'r') as arquivo:
    data_source = json.load(arquivo)

#autenticaçaõ da API
url = 'https://api.gotit.ai/NLU/v1.5/Analyze'
userAndPass = base64.b64encode(b"sua_chave_para_processamento").decode("ascii")
headers = {'Content-type': 'application/json', "Authorization": "Basic %s" %  userAndPass}



#estabelece range de mensagens para serem processadas
for n in range(6001,14342):

    data_request = {
        "T": (data_source[str(n)]["message"]).strip(),
        "S": True,
        "EM": True
    }

    print("Request ", n)
    response = requests.post(url, data=json.dumps(data_request), headers=headers)

    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        print(f"Resposta recebida! Gravando!")
        data_source[str(n)].update(response.json())
        
    else:
        print("Falha na requisição", response)


    # Salvar o dicionário atualizado de volta em um arquivo JSON
    with open('mensagem_atualizada.json', 'w') as json_file:
        json.dump(data_source, json_file, indent=4)

    print("JSON atualizado salvo com sucesso.")

