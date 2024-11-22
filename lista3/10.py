class Temperatura:
    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# Exemplo de uso:
temperatura = Temperatura()
print(temperatura.celsius_para_fahrenheit(25))
