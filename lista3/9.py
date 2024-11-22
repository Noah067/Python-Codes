class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def status(self):
        if self.nota >= 7:
            return f"{self.nome} está aprovado!"
        else:
            return f"{self.nome} está reprovado!"

# Exemplo de uso:
aluno = Aluno("Maria", 8)
print(aluno.status())
