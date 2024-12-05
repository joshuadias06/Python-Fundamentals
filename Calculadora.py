print("===================================================")
print("===================================================")
print("====================CALCULADORA====================")
print("=================( + , - , * , /)=================")
print("===================================================")
print("===================================================")


continuar = True

while continuar:
    print("Escolha uma operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    
    operacao = int(input("Opção de 1 a 5:"))
    
    if operacao <= 0 or operacao > 5:
        print("Escolha um opção entre 1 e 5: ")
    elif operacao == 1:
        posicao1 = float(input("Digite o primeiro valor:"))
        posicao2 = float(input("Digite o segundo valor: "))
        soma = posicao1 + posicao2
        print(soma)
    elif operacao == 2:
        posicao1 = float(input("Digite o primeiro valor:"))
        posicao2 = float(input("Digite o segundo valor: "))
        menos =  posicao1 - posicao2
        print(menos)
    elif operacao == 3:
        posicao1 = float(input("Digite o primeiro valor:"))
        posicao2 = float(input("Digite o segundo valor: "))
        multiplicao = posicao1 * posicao2
        print(multiplicao)
    elif operacao == 3:
        posicao1 = float(input("Digite o dividendo: "))
        posicao2 = float(input("Digite o divisor: "))
        quociente = posicao1 / posicao2
        print(quociente)
    elif operacao == 5:
        print("Saindo...")
        break