class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

# Exemplo de uso:
livro = Livro("1984", "George Orwell")
livro.exibir_detalhes()
