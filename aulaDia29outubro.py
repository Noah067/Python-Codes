# time = ['1-Palmeiras','2-Curitiba','3-São Paulo']
# for n in time:
#     print(n)




# soma=0
# x=int(input("first number = "))
# y=int(input("second number = "))
# for i in range(x,y+1):
#     print(i)
#     soma = soma+i
# print(soma)




# for i in range (1,20+1):
#     print(i, end= " ")


# cont = 0
# soma = 0
# for x in range(5):
#     n1 = int(input("Digite um número = "))
#     soma = soma+n1
#     cont = cont+1
# print(soma)

# media=soma/cont
# print(media)




def fibonacci(n):
    fib_sequencia = [0, 1]
    for i in range(2, n):
        proximo_valor = fib_sequencia[i - 1] + fib_sequencia[i - 2]
        fib_sequencia.append(proximo_valor)
    return fib_sequencia[:n]


n = int(input("Digite a quantidade de fibonacci = "))  # Número de termos que eu quero na sequência!!!!!!!
print(fibonacci(n))