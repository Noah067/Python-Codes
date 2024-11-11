def ocorrencias_palavras(texto):
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.lower()  # Ignorar diferenças de maiúsculas e minúsculas
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

print(ocorrencias_palavras(texto))