"""
Exercício
Crie funções que duplicam triplicam e quadriplicam
o número recebido como parâmetro
"""

def funcao(numero = input("Digite um número")):

    def dobro():
        conta = int(numero) * 2
        print(conta)
        return conta
        
    def triplica():
            conta = int(numero) * 3
            print(conta)
            return conta
    
    def quadriplica():
         conta = int(numero) * 4
         print(conta)
         return conta
    
    quadriplica()
    triplica()
    dobro()
funcao()


