class Aluno():
    # Método construtor
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

aluno1 = Aluno("Allan",100)
print(aluno1.nome)
print(aluno1.idade)


aluno2 = Aluno("Paulo",150)
print(aluno2.nome)
print(aluno2.idade)
