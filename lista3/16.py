class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, outra_pessoa):
        print(f"Olá, {outra_pessoa.nome}!")

# Exemplo de uso:
pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")
pessoa1.cumprimentar(pessoa2)
