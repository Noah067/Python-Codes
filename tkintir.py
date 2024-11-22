import customtkinter as ctk
janela = ctk.CTk()
janela.geometry('240x240')
ctk.set_appearance_mode('dark')
texto = ctk.CTkLabel(janela,text=("Ola Mundo!"))
texto.pack()
numero = ctk.CTkEntry(janela, placeholder_text=("Digite um numero = "))
numero.pack()
botao = ctk.CTkButton(janela, text=("Salve"))
botao.pack()
x = botao.place(x=50,y=70)
janela.destroy



janela.mainloop()