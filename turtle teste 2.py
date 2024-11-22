# import turtle

# turtle.setup(900, 900)


# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# turtle.penup() #levanta caneta

# turtle.goto(100,100) # vai para a posição

# turtle.pendown() # abaixa a caneta

# turtle.circle(50,360) # faz o circulo

# turtle.done() # finalizar o progaminha da tartaruguinha




import turtle

# Configuração inicial da tela
screen = turtle.Screen()
screen.bgcolor("white")

# Criação da tartaruga
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)  # A velocidade é a mais rápida para animação contínua

# Cor da tartaruga
t.color("blue")

# Começa a desenhar a espiral
for i in range(100):
    t.forward(i * 10)  # Move a tartaruga para frente, com um aumento gradual
    t.right(45)         # Gira a tartaruga para a direita


turtle.done()