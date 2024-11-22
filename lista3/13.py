class Veiculo:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

    def aumentar_velocidade(self, incremento):
        self.velocidade += incremento

# Exemplo de uso:
veiculo = Veiculo("Fusca", 60)
veiculo.aumentar_velocidade(20)
print(f"Velocidade: {veiculo.velocidade} km/h")
