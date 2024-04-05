# Caminho do arquivo que você deseja processar
caminho_do_arquivo = 'dados.txt'
arquivo_saida = 'saida.csv'
novas_linhas = []

# Abre o arquivo para leitura e lê as linhas
with open(caminho_do_arquivo, 'r', encoding="utf8") as arquivo:
    linhas = arquivo.readlines()

    # Filtra as linhas, removendo as que são apenas espaços em branco
    for linha in linhas:
        nova_linha = linha[:8] + ";" + linha[8:]
        novas_linhas.append(nova_linha)
        



# Abre o arquivo para escrita e escreve as linhas filtradas
with open(arquivo_saida, 'w', encoding="utf8") as arquivo:
    arquivo.writelines(novas_linhas)

