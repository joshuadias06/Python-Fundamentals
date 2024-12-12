def fabrica_de_operacoes(operacao, *args):

    def soma ():
        soma = sum(args)
        return soma

    def subtracao ():
        if len(args) == 2:
            return args[0] - args[1]
        else:
            sub = args[0]
            for i in range(1, len(args)):
                sub -= args[i]

        return sub

    def multiplicacao ():

        if len(args) == 2:
            return args[0] * args[1]
        else:
            multiplicacao = 1
            for i in range(1, len(args)):
                multiplicacao *= args[i]
        return multiplicacao

    def divisao ():
        if len(args) == 2:
            return args[0] / args[1]
        else:
            divisao = args[0]
            for i in range(1, len(args)):
                divisao /= args[i]
        return divisao

    if operacao == '1':
        return soma()
    elif operacao == '2':
        return subtracao()
    elif operacao == '3':
        return multiplicacao()
    elif operacao == '4':
        return divisao()


print("----------------------\n")
print("MENU")
print("1. Soma")
print("2. Subtracao")
print("3. Multiplicacao")
print("4. Divisao")
print("5. Sair")
print("\n----------------------")

while True:
    opc = int(input("Digite uma opcao de 1 a 5:"))
    if opc < 0 or opc > 5:
        print("Opcao invalida!")
        continue
    elif opc == 1:
        nums = list(map(float, input("Digite os numeros para serem somados separados por um espaco: ").split()))
        resposta = fabrica_de_operacoes("1", *nums)
        print(resposta)
        continue
    elif opc == 2:
        nums = list(map(float, input("Digite os numeros para serem subtraidos separados por um espaco: ").split()))
        resposta = fabrica_de_operacoes("2", *nums)
        print(resposta)
        continue
    elif opc == 3:
        nums = list(map(float, input("Digite os numeros para serem multiplicados separados por um espaco: ").split()))
        resposta = fabrica_de_operacoes("3", *nums)
        print(resposta)
        continue
    elif opc == 4:
        nums = list(map(float, input("Digite os numeros para serem dividos separados por um espaco: ").split()))
        resposta = fabrica_de_operacoes("4", *nums)
        print(resposta)
        continue
    elif opc == 5:
        print("Saindo...")
        break