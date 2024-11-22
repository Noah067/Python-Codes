class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"

# Exemplo de uso:
data = Data(5, 11, 2024)
print(data.formatar())
