lista = []

while True:
    print("Selecione uma opção)
    opcao = input("[i]nserir, [a]pagar, [l]istar")

    if opcao == "i":
      os.system("clear")
      valor = input("Valor: ")
      lista.append(valor)
