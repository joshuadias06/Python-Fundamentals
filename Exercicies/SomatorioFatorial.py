def fatorial(n):
    for i in range (1, n):
        n *= i

    return n


somaFat = 0

while True:

    print("\n----------------------------")
    print("1. Digitar um fatorial: ")
    print("2. Sair")

    opc = int(input("Digite um opção: "))

    if opc < 0 or opc > 2:
        print("OPÇÃO INVÁLIDA!")
        continue
    elif opc == 1:
        num = int(input("Digite um fatorial: "))
        resultado = fatorial(num)
        somaFat += resultado
        print(f"FATORIAL: {resultado}")
        print(f"SOMA FATORIAL: {somaFat}")
        continue
    elif opc == 2:
        print
