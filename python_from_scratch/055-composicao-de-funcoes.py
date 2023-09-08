def fazerlogin():
    print("Login realizado com sucesso!")

def errologin():
    print("Erro no login")

def tentarlogar(login,senha):
    logincorreto="login1"
    senhacorreta = "senha1"
    if((login == logincorreto) and (senha == senhacorreta)):
        fazerlogin()
    else:
        errologin()


tentarlogar("login1","senha1")