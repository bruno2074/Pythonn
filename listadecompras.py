"""

Todas as variáveis nos comentários estão entre aspas ("x")
"""
import os

lista = []

# cria uma condição que repete infinitamente até ser quebrada por algum "break"
while True:
    # pede opcao 
    print('Selecione uma opção')
    # recebe opcao
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    # se opcao for [i]:
    if opcao == 'i':
        # apaga terminal e pede "valor"
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)

    # recebe opcao 
    elif opcao == 'a':
        # pede índice da lista para apagar
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        # abre um bloco pra verificação de erros em relação ao índice [a]  
        try:
            indice = int(indice_str)
            del lista[indice]
        # Error caso o número seja float
        except ValueError:
            print('Por favor digite número int.')
        # Error caso índice não estiver na lista
        except IndexError:
            print('Índice não existe na lista')
        # Error caso não saiba a definição do erro
        except Exception:
            print('Erro desconhecido')
    # Recebe opção 
    elif opcao == 'l':
        os.system('clear')
        # Caso a lista tenha 0 índices, apresenta o print "Nada para listar"
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
