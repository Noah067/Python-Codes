import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

# Exemplo de uso:
circulo = Circulo(5)
print(f"Perímetro do círculo: {circulo.calcular_perimetro()}")
