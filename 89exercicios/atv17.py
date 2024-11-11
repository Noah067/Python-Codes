texto = input("Digite um texto: ")
palavra = input("Digite uma palavra: ")
def encontra_palavra(texto, palavra):
    palavras = texto.split()
    for i, p in enumerate(palavras):
        if p == palavra:
            return i
    return -1  # Retorna -1 se a palavra não for encontrada

# Testando a função
print(encontra_palavra(texto, palavra))