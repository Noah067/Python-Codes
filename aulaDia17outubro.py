# a = float(input("Digite um numero = "))
# while a<100:
#     print("Menor")
# print("Fim")




# while True:
#     print("Loop infinito\n")




# while True:
#     valor = int(input("Digite 1 ou 0 para fim = "))
#     if valor ==1:
#         print("Valor correto")
#     elif valor == 0:
#         print("Valor para sair")
#         break




# num = int(input("Digite um valor = "))
# cont = 0
# while num >= 0:
#     cont= cont+1
#     num=num-1
# print(cont)




# i = 0
# while i==0:
#     opcao = int(input("Escolha uma das opções abaixo:\n1-multiplicação\n2-divisão\n3-adição\n4-subtração\n5-sair\n"))
                      
#     if opcao==1:
#         a1=float(input("Digite o primeiro valor = "))
#         a2=float(input("Digite o segundo valor = "))
#         a3=a1*a2
#         print("O resultado é = ",a3)

#     elif opcao==2:
#         a1=float(input("Digite o primeiro valor = "))
#         a2=float(input("Digite o segundo valor = "))
#         a3=a1/a2
#         print("O resultado é = ",a3)

#     elif opcao==3:
#         a1=float(input("Digite o primeiro valor = "))
#         a2=float(input("Digite o segundo valor = "))
#         a3=a1+a2
#         print("O resultado é = ",a3)
        
#     elif opcao==4:
#         a1=float(input("Digite o primeiro valor = "))
#         a2=float(input("Digite o segundo valor = "))
#         a3=a1-a2
#         print("O resultado é = ",a3)

#     elif opcao==5:
#         print("Saindo...")
#         i=1

#     else:
#          print("Não existe essa opção!")
#          break
    




# while True:

#     nota = int(input("Digite sua nota = "))

#     if nota >= 0 and nota <= 10:
#         print("Valor é valido!")
#         break
#     else:
#         print("Esse numero é invalido!")
        



# while True:

#      name = str(input("Digite seu nome = "))
#      senha = str(input("Digite sua senha = "))
     
#      if senha != name:
#         print("Password Sucefully")
#         break 
     
#      elif senha == name:
#           print("Senha não pode ser igual o nome!")



while True:
    nome = str(input("Digite seu nome = "))
    
    if len(nome)>3:
        print("Seu nome é = ",nome)
        print("Nome aceito!")
        break
    else:
        print("Nome invalido!")


while True:
    idade = int(input("Digite sua idade = "))

    if idade >= 0 and idade < 151:
        print("Sua idade é = ",idade)
        print("idade valida!")
        break
    else:
        print("Idade invalida!")

while True:
    salario = float(input("Digite seu salário = "))

    if salario > 0:
        print("Seu salário é = ",salario)
        break
    else:
        print("Salario invalido!")

while True:
    