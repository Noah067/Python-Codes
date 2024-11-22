class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)

# Exemplo de uso:
funcionario = Funcionario("José", 1500)
funcionario.calcular_aumento(10)
print(f"Novo salário: {funcionario.salario}")
