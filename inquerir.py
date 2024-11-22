from InquirePy import inquirer

nome = inquirer.text('qual é o seu nome = ').execute()
cor = inquirer.select('qual é a sua cor predileta = ',choices ["Azul","Vermelho"] = ").execute