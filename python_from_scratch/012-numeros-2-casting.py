n1 = 3
n2 = 2

divisao = n1 / n2

print("Divisão")
print(divisao)
print(type(divisao))

print("N1")
print(type(n1))

# Casting
print("Testes com o casting")
n2 = float(n1)
print(n2)
print(type(n2))

divisao_int = int(divisao)
print(divisao_int)
print(type(divisao_int))

# Casting com Strings
mensagem = "O resultado da divisão é: " + str(divisao)
print(mensagem)