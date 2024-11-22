class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def verificar_altura(self):
        if self.altura > 1.75:
            return f"{self.nome} é mais alto que 1,75m."
        else:
            return f"{self.nome} não é mais alto que 1,75m."

# Exemplo de uso:
pessoa = Pessoa("Carlos", 1.80)
print(pessoa.verificar_altura())
