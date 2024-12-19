def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

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
    elif opc == 1:
        a =int(input("Digite um valor:"))
        b = int(input("Digite outro valor:"))
        print(soma(a, b))
        continue
    elif opc == 2:
        a =int(input("Digite outro valor:"))
        b = int(input("Digite outro valor:"))
        print(subtracao(a, b))
        continue
    elif opc == 3:
        a =int(input("Digite outro valor:"))
        b = int(input("Digite outro valor:"))
        print(multiplicacao(a, b))
        continue
    elif opc == 4:
        a =int(input("Digite outro valor:"))
        b = int(input("Digite outro valor:"))
        print(divisao(a, b))
        continue
    elif opc == 5:
        print("Saindo...")
        break

