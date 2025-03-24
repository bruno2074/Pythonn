"""
Exercício
Crie funções que duplicam triplicam e quadriplicam
o número recebido como parâmetro
"""

def funcao(numero=input("Digite um número")):

    def multiplicacao(multiplicador = input
    ("Digite por quanto quer multiplicar: ")):

        conta = int(numero) * int(multiplicador)
        print(conta)
        return conta
    multiplicacao()

funcao()
