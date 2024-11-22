class Eletrodomestico:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia

    def ligar(self):
        print(f"{self.nome} está ligado.")

# Exemplo de uso:
eletrodomestico = Eletrodomestico("Liquidificador", 300)
eletrodomestico.ligar()
