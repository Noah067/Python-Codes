class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_hora(self):
        return f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"

# Exemplo de uso:
relogio = Relogio(10, 45, 30)
print(relogio.exibir_hora())
