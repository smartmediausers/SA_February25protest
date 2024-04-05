# Caminho do arquivo que você deseja processar
caminho_do_arquivo = 'dados.txt'

# Abre o arquivo para leitura e lê as linhas
with open(caminho_do_arquivo, 'r', encoding="utf8") as arquivo:
    linhas = arquivo.readlines()

# Filtra as linhas, removendo as que são apenas espaços em branco
linhas_filtradas = [linha for linha in linhas if linha.strip()]

# Abre o arquivo para escrita e escreve as linhas filtradas
with open(caminho_do_arquivo, 'w', encoding="utf8") as arquivo:
    arquivo.writelines(linhas_filtradas)
