naosourobo = False
emailexistente = True
senhacorreta = 'senha1'

senhadigitada = input("Qual é a sua senha: ")

if(naosourobo):
    if(emailexistente):
        if(senhadigitada == senhacorreta):
            print("Você acessou o sistema")
        else:
            print("Você digitou a senha errada")
    else:
        print("Email inexistente")
else:
    print("Você é um robô e, portanto, não pode acessar o sistema!")