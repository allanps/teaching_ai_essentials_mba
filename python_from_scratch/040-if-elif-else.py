emailexistente = True
senhacorreta = 'senha1'

senhadigitada = input("Qual é a sua senha: ")

if not emailexistente:
    print("Este e-mail não existe")
elif (senhadigitada != senhacorreta):
    print("Senha incorreta")
else:
    print("Tudo certo, você pode acessar o sistema")
