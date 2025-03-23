import os
import random
import string

resposta_input = input("Você quer criar uma senha? S/n")

if resposta_input == "S":
    # Define que caractéres podem ser:
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    caracteres = string.ascii_letters + string.digits
    # cria variável que recebe a senha
    senha = ''
    for i in range(13):
        senha += random.choice(caracteres)
    
    print(senha)

else:
    print("Sem senha")
    os.system("clear")
