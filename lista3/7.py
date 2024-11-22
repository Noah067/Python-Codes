class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        self.preco -= self.preco * desconto / 100

# Exemplo de uso:
produto = Produto("Camiseta", 50)
produto.aplicar_desconto(10)
print(f"Preço com desconto: {produto.preco}")
