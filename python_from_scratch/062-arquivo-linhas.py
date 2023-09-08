caminho = "arquivo.txt"

arquivo = open(caminho)

for linha in arquivo:
    print(linha)

arquivo.close()