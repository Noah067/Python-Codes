class Carro:
    def __init__(self, marca, combustivel):
        self.marca = marca
        self.combustivel = combustivel

    def abastecer(self, quantidade):
        self.combustivel += quantidade

    def verificar_combustivel(self):
        return f"Nível de combustível: {self.combustivel} litros"

# Exemplo de uso:
carro = Carro("Fiat", 50)
carro.abastecer(20)
print(carro.verificar_combustivel())
