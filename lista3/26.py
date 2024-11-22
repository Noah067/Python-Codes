class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"Soma: {a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"Subtração: {a} - {b} = {resultado}")
        return resultado

    def exibir_historico(self):
        for operacao in self.historico:
            print(operacao)

# Exemplo de uso:
calculadora = Calculadora()
calculadora.somar(3, 2)
calculadora.subtrair(10, 5)
calculadora.exibir_historico()
