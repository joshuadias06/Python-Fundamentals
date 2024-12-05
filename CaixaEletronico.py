# CAIXA ELETRONICO BASICO (CONSULTA DE SALDO, DEPOSITO, SAQUE e SAIR DO PROGRAMA)

continuar = True
saldo = 1000.0

while continuar:
    print("\n1 - Consulta")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Sair")

    try:
        opc = int(input("Digite uma opção de 1 a 4: "))

        if opc <= 0 or opc > 4:
            print("Digite uma opção válida!")
        elif opc == 1:
            print(f"Seu saldo atual é: R${saldo:.2f}")
        elif opc == 2:
            deposito = float(input("Digite o valor a ser depositado: "))
            saldo += deposito
            print(f"Depósito realizado! Novo saldo: R${saldo:.2f}")
        elif opc == 3:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque > saldo:
                print("Saldo insuficiente!")
            else:
                saldo -= saque
                print(f"Saque realizado! Novo saldo: R${saldo:.2f}")
        elif opc == 4:
            print("Saindo...")
            continuar = False
    except ValueError:
        print("Por favor, digite uma opção válida!")
