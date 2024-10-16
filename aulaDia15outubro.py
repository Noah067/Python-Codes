# bi1 = float(input("Escreva sua nota do 1º Bimestre = "))
# bi2 = float(input("Escreva sua nota do 2º Bimestre = "))

# bi3 = (bi1+bi2)/2
# print("Sua média é = ",bi3)

# if bi3 ==10:
#     print("Aprovado com distinção")
# elif bi3 >= 7:
#     print("Aprovado")
# else:
#     print("reprovado")



#-------------------------------------------------------------------



# salario = float(input("digite um valor = "))



# if salario <= 280:
#     porcentagem = 20

# elif salario >= 280 and salario < 700:
#     porcentagem = 15
    
# elif salario >= 700 and salario < 1500:
#     porcentagem = 10

# elif salario >= 1500:
#     porcentagem = 5


# aumento = salario*porcentagem/100
# total = aumento + salario

# print(porcentagem, "<--- porcentagem")
# print(salario, "<--- salário anterio")

# print(aumento, "<---- aumento")
# print(total, "<--- total")


#------------------------------------------------------------------



# nota1 = float(input"(escreva sua nota do 1º bimestre = "))
# nota2 = float(input"(escreva sua nota do 2º bimestre = "))
# nota3 = float(input"(escreva sua nota do 3º bimestre = "))
# nota4 = float(input"(escreva sua nota do 4º bimestre = "))

# media = (nota1+nota2+nota3+nota4)/4

# if media ==9.1 and media <= 10.0:
#     print("sua media é \nAPROVADO")
# elif media ==7.6 and media <= 9.0:
#     print("sua media é \nAPROVADO")
# elif media == 6.0 and media <= 7.5:
#     print("sua media é \nAPROVADO")
# elif media ==4.1 and media <= 5.9:
#     print("sua media é \REPROVADO")
# elif media == 4.0 and media <= 0.0:
#     print("sua media é \REPROVADO")

#-----------------------------------------------------------------pergunta1



pergunta1 = input("Telefonou para vitima? = ")
pergunta2 = input("Esteve no local do crime? = ")
pergunta3 = input("Mora perto da vitima? = ")
pergunta4 = input("Devia para vitima? = ")
pergunta5 = input("Ja trabalhou com a vitima? = ")

count = 0
if pergunta1== "Sim":
    count= +1
if pergunta2== "Sim":
    count= +1
if pergunta3== "Sim":
    count= +1
if pergunta4== "Sim":
    count= +1
if pergunta5== "Sim":
    count= +1

if count == 5:
    print("assasina")
elif count == 4 or count==3:
    print("cumplice")
elif count ==2:
    print("suspeito")
elif count ==1 or count == 0:
    print("inocente")