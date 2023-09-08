emailexistente = True
senhacorreta = 'senha1'

senhadigitada = input("Qual é a sua senha: ")

if not emailexistente:
    print("Este e-mail não existe")
elif (senhadigitada != senhacorreta):
    pass
else:
    print("Tudo certo, você pode acessar o sistema")
