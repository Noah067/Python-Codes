class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append((nome, telefone))

    def listar_contatos(self):
        for nome, telefone in self.contatos:
            print(f"{nome}: {telefone}")

# Exemplo de uso:
agenda = Agenda()
agenda.adicionar_contato("João", "12345")
agenda.adicionar_contato("Maria", "67890")
agenda.listar_contatos()
