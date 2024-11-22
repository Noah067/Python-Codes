class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao} minutos")

# Exemplo de uso:
filme = Filme("O Poderoso Chefão", 175)
filme.exibir_detalhes()