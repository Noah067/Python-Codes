class Elevador:
    def __init__(self, total_andares):
        self.andar_atual = 1
        self.total_andares = total_andares

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        else:
            print("Já está no último andar.")

    def descer(self):
        if self.andar_atual > 1:
            self.andar_atual -= 1
        else:
            print("Já está no térreo.")

# Exemplo de uso:
elevador = Elevador(5)
elevador.subir()
print(f"Andar atual: {elevador.andar_atual}")
