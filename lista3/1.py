class Pessoa:
    def __init__(self, name, idade):
        self.name = name

        self.idade = idade



    def __str__(self):
        return f"Name: {self.name}, Idade: {self.idade}"
    

p = Pessoa("Abel", 16)
print(p)