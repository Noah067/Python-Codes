class ConversorMoeda:
    @staticmethod
    def dolar_para_real(dolares, taxa=5.0):
        return dolares * taxa

# Exemplo de uso:
conversor = ConversorMoeda()
print(conversor.dolar_para_real(100))
