texto = input("Digite um texto: ")
def capitaliza_palavras(texto):
    palavras = texto.split()
    palavras_capitalizadas = [palavra.capitalize() for palavra in palavras]
    return ' '.join(palavras_capitalizadas)

print(capitaliza_palavras(texto))