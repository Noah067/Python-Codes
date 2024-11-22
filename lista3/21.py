class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo
        self.autor = autor
        self.estoque = estoque

    def exibir_estoque(self):
        print(f"Estoque de '{self.titulo}': {self.estoque} unidades")

# Exemplo de uso:
livro = Livro("1984", "George Orwell", 12)
livro.exibir_estoque()
