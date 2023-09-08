caminho = "arquivo.txt"

# arquivo = open(caminho,"w")
# arquivo.write("Outro texto")
# arquivo.close()

with open(caminho,"w") as arquivo:
    arquivo.write("Mais um texto")