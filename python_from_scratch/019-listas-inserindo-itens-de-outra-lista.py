dados = ["el1", "el2", "el3"]
dados_adicionais = ["el4", "el5"]

print("Antes do extend")
print(dados)
print(dados_adicionais)

dados.extend(dados_adicionais)

print("\nDepois do extendo")
print(dados_adicionais)
print(dados)
