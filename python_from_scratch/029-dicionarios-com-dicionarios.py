acessos = {
    '1' : {
        'paginasvisitadas' : ['inicial','especifica1','especifica2'],
        'comprou': ['produto1','produto2']
    },
    '2' : {
        'paginasvisitadas' : ['inicial','especifica1'],
        'comprou' : ['produto1'],
        'cliquesembotoes' : ['btn1','btn2']
    }
}

print(acessos)
print("\nUsuário 1")
print(acessos['1'])
print("\nUsuário 2")
print(acessos['2'])

print("\nPáginas visitadas pelo usuário 1")
print(acessos['1']['paginasvisitadas'])
print("\nPáginas visitadas pelo usuário 2")
print(acessos['2']['paginasvisitadas'])

print("\nPrimeira página visitadas pelo usuário 1")
print(acessos['1']['paginasvisitadas'][0])
print("\nPrimeira página visitadas pelo usuário 2")
print(acessos['2']['paginasvisitadas'][0])
