# empresas = (1,2,3,4,5)
# empresas1 = (6,7,8,9,10)
# print(empresas+empresas1)




#------------------------------------------------------------





# empresas = ("Brasil", "EUA","Canada","Rússia")
# print(empresas.index("Rússia"))




#-------------------------------------------------------------




# li = [[1,2],[3],[4,5,6]]
# print(type(li))




#-------------------------------------------------------------




# tu = (1,2,3,4,5,6,'a','b','c')
# tu = (list(tu))
# print(type(tu))




#------------------------------------------------------------




#   Descrição         |   Operador
# _____________________________________
#   Maior que         |   >
#   Menor que         |   <
#   Igual a           |   ==
#   Maior ou igual a  |   >=
#   Menor ou igual a  |   <=




# x = 90.1 
# if x > 90:
#     print("X é maior que 90")
#     print("X é maior que 90")
#     print("X é maior que 90")
#     print("X é maior que 90")
#     print("X é maior que 90")
#     print("X é maior que 90")
#     print("X é maior que 90")
#     print("X é maior que 90")
# print("Termino")



#-----------------------------------------------------



# age = 18
# if (age>17):
#     print('você é maior, já pode dirigir!')
# print('fim, fora do if')



#----------------------------------------------------




# idade = int(input("Digite sua idade = "))
# if idade >=18: #Caso verdadeiro
#     print("Maior de idade")
# else: #Caso falso
#     print("Menor de idade")



#-----------------------------------------------------



# idade = int(input("Digite sua idade = "))
# if idade ==16: #Caso verdadeiro
#     print('Pode votar!')
# else:
#     if idade >=18:
#         print('Pode dirigir, votar e continuar estudando!')
#     else:
#         if idade <16:
#             print('Apenas estude!')




#------------------------------------------------------


# idade = int(input("Digite o ano que voce nasceu = "))
# if idade <=2008:
#     print('Pode votar')
# else:
#     if idade >2008:
#         print('Voce ainda nao pode votar')




#--------------------------------------------------------



# maca1 = 0.30
# maca2 = 0.25
# zx = float(input('Quantidade de maçãs = '))

# if zx <12:
#     print(zx*maca1)
# else:
#     if zx >=12:
#         print(zx*maca2)



#----------------------------------------------------------



# a = int(input('Digite um numero = '))
# b = int(input('Digite um numero = '))
# c = int(input('Digite um numero = '))

# if a<b and b<c:
#     print(a,b,c)
# elif a<b and b<c:
#     print(a,c,b)

# elif b>a and b<c:
#     print(b,c,a)
# elif b>a and b<c:
#     print(b,a,c)

# elif c>a and c>b:
#     print(c,a,b)
# elif c>a and c>a:
#     print(c,b,a)
