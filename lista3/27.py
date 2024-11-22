class Animal:
    def __init__(self, especie, movimento):
        self.especie = especie
        self.movimento = movimento

    def mover(self):
        print(f"O {self.especie} {self.movimento}")

# Exemplo de uso:
animal = Animal("Peixe", "nada")
animal.mover()
