acesso = {
    'idpessoa':'1',
    'paginasvisitadas' : ['inicial','especifica1','especifica2'],
    'comprou': ['produto1','produto2']
    }

print(acesso)
print("\nPáginas visitadas:")
print(acesso['paginasvisitadas'])

print("\nPrimeira página visitada:")
print(acesso['paginasvisitadas'][0])
