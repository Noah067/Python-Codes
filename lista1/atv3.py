def eh_par (x):
     if (x %2) ==0:
         return True
     else:
         return False
while True:
     num = int(input("Digite um nº: "))
     if eh_par(num):
         print("É par")
     else:
         print("É ímpar")