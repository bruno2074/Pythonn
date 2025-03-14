# Calculadora com while


resposta = input("Quer calcular? [S/s]").lower().startswith('s''S')
calcular = 'S' or 's'
if resposta == calcular:
    while calcular is True:
        numero1 = input("Digite um número\n")
        numero2 = input("Digite ouStro número")
        numerofloat1 = float(numero1)
        numerofloat2 = float(numero2)
        operacao = input("Qual a operação que você quer fazer").lower().startswith('soma' 'subtração' 'multiplicação' 'divisão')
    
    if operacao is True: 
        calculo = numerofloat1 + numerofloat2
        print(calculo)

    numero_valido = None
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)

    except:
        numero_valido = None

    if numero_valido is None:
        print("Digito inválido")

    if calcular is False:
        sair = input("Quer [s]air?").lower().startswith('s')
        if sair is True:
            print("obrigado")
        
