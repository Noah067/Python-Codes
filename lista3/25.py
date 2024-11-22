class Pessoa:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

# Exemplo de uso:
pessoa = Pessoa(1.80, 75)
print(f"IMC: {pessoa.calcular_imc()}")
