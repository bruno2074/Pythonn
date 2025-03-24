""" 
Exercício com funções 

Crie uma função que multiplica todos
os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre
o valor da variável
"""
def multiplicar (*args):
    total = 1 
    for numero in args:
        total *= numero
        return total
    
multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)

"""
Crie uma função que fala se um número
é par ou ímpar
Retorne se o número é par ou ímpar
"""

numero1 = int(input("Digite um número"))

divisao = numero1 % 2
if divisao >= 1:
    print("Esse número é impar")
else:
    print("Esse número é par")
