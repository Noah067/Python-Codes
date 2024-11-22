class Jogo:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao

    def iniciar_jogo(self):
        print(f"Iniciando o jogo: {self.nome}")

    def registrar_pontuacao(self, pontuacao):
        self.pontuacao = pontuacao

# Exemplo de uso:
jogo = Jogo("Mario", 0)
jogo.iniciar_jogo()
jogo.registrar_pontuacao(1500)
print(f"Pontuação: {jogo.pontuacao}")
