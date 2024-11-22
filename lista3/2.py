class Retangulo:


    def __init__(self, alt, larg):

     self.altura = alt
       
        
     self.largura = larg


    def calcular_area(self):
        return  self.altura * self.largura
    
ret = Retangulo(4, 5)
print(f"Área do retângulo: {ret.calcular_area()}")