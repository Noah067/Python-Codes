class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_saldos(self):
        for conta in self.contas:
            print(f"Saldo da conta: {conta.saldo}")

# Exemplo de uso:
banco = Banco()
conta1 = ContaBancaria(1000)
conta2 = ContaBancaria(1500)
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.listar_saldos()
