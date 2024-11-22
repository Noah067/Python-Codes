
# '''27. Verifica Ordem Crescente: Crie uma função esta_ordenada(lista) que verifica se uma 
# lista está ordenada em ordem crescente.'''

def esta_ordenada(lista):
    # Percorre a lista e compara cada elemento com o próximo
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
print(esta_ordenada([1, 2, 3, 4, 5]))  # True
print(esta_ordenada([1, 3, 2, 4, 5]))  # False
print(esta_ordenada([5, 4, 3, 2, 1]))  # False
print(esta_ordenada([1, 1, 1, 1, 1]))  # True