while True:
    numero_1 = input("Digite um numero: \n")
    numero_2 = input("Digite outro número:")
    operador = input("Digite o operador (+-/*): ")

# Criando uma flag
    numeros_validos = None

# Entrando no try/except
    try:
        # Tenta converter numero_1 para float
        num_1_float = float(numero_1)
        # Tenta converter numero_2 para float
        num_2_float = float(numero_2)
        # Não gerou erro? então numeros_validos = True
        numeros_validos = True    
    
    # except será utilizado caso haja erro na conversão para float
    except:
        numeros_validos = None
    # Checa se numeros_validos ainda é none, caso for, apresenta a mensagem
    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos. ")
        # final do laço, caso exista algum número errado voltará o código lá nas perguntas 
        continue

    operadores_permitidos = "+-/*"
# caso usuário tiver digitado qualquer coisa fora do esperado:
    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue
# caso usuário tiver digitado mais de um operador
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue
    
    print("Realizando sua conta. Confira o resultado abaixo: ")

    if operador == "+":
        print(num_1_float + num_2_float)
    elif operador == "-":
        print(num_1_float - num_2_float)
    elif operador == "*":
        print(num_1_float * num_2_float)
    elif operador == "/":
        print(num_1_float / num_2_float)
    else:
        print("Nunca deveria chegar aqui")

    sair = input("Quer [s]air: ").lower().startswith('s')
    
    if sair is True:
        break
