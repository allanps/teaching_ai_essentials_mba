def tentarlogar(login,senha):
    logincorreto = 'login1'
    senhacorreta = 'senha1'
    if((login == logincorreto) and (senha == senhacorreta)):
        print("Login realizado com sucesso")
    else:
        print("Erro no login")

tentarlogar("senha1","login1")
