afirmacao1 = 1 != 1
afirmacao2 = 2 < 1

print(afirmacao1)
print(afirmacao2)
print(afirmacao1 and afirmacao2)


print("\nLidando com senha e email")
senhadigitada = 'senha1'
senhacorreta = 'senha1'
senhavalida = senhadigitada == senhacorreta
emailvalido = True
podefazerlogin = False
print(senhavalida and emailvalido and podefazerlogin)
