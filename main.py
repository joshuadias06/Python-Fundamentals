"""
posicaoLetra = "Python"
print(posicaoLetra[0])
print(posicaoLetra[1])
print(posicaoLetra[2])
print(posicaoLetra[3])
print(posicaoLetra[4])
print(posicaoLetra[5])

frase = "Ola, mundo!"
parte = frase[4:8]
print(parte)

primeiros = frase[:5]
print(primeiros)

ultimos = frase[-6:]
print(ultimos)

frase1 = "Python e legal"
print("Python" in frase1)


frase2 = "Python e legal"

if "Python" in frase2:
    print("Sim tem Python na frase")

frase2 = "        Python e legal         "
print(frase2)
print(frase2.strip())

frase3 ="ola como vai?"
palavras = frase3.split()

print(palavras)

palavras1 = ["oi," "tudo bem"]
frase4 = ''.join(palavras1)
print(frase4)

texto = "************Ola!*************"
texto_strip = texto.strip('*')
print(texto_strip)
"""

"""nome ="Queren"
idade = 21
altura = 1.60
#f = Format Strings
mensangem = f"Ola, meu nome e {nome}. Tenho {idade} e {altura:.2f} de altura"
print(mensangem)"""


"""
texto = "Ola Mundo"
texto_upper = texto.upper()
print(texto_upper)

texto_lower = texto.lower()
print(texto_lower)

texto_cap = texto.capitalize()
print(texto_cap)

ocorrencias = texto.count("o")
print(ocorrencias)

texto_subs = texto.replace("Mundo", "Amigo")
print(texto_subs)
"""

"""nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

nome_completo = nome + " " + sobrenome
mensagem = f"Seu nome: {nome_completo}. Sua idade: {idade}"

print(mensagem)"""

"""frase = "Python e uma linguagem de programcao poderosa e versatil"
print(len(frase))
palavra = frase.split()[0]
print(palavra)

frase_maiuscula = frase.upper()
print(frase_maiuscula)

texto_subs = frase.replace("poderosa", "incrivel")
print(texto_subs)"""


"""idade = 60# Altere esse valor para testar diferentes faixas etárias

# Escreva sua estrutura condicional abaixo

if idade == 0:
    print("Digite uma idade valida")
elif idade <= 12:
    print("Acesso Para Criancas Permitido")
elif idade >= 13 and idade <= 17:
    print("Acesso Para Adolecentes Permitido")
elif idade >= 18 and idade <= 59:
    print("Acesso Para Adultos Permitido")
elif idade >= 60:
    print("Acesso Para Idosos Permitido")"""



#APOSTA
"""import random


numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")


while not acertou:
   
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1


    if palpite == numero_secreto:
        acertou = True
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
        if tentativas == 10:
            acertou = True
        continuar = input("Deseja continuar? [s/n] ")
        if continuar == "s":
            acertou = False
        else:
            acertou = True
    else:
        print("O número secreto é menor. Tente novamente.")
        if tentativas == 10:
            acertou = True
        continuar = input("Deseja continuar? [s/n] ")
        if continuar == "s":
            acertou = False
        else:
            acertou = True"""

#SENHA MUITO BASICO
"""secreto = "Saxalto@1101."
senha = input("Digite sua senha: ")

while senha != secreto:
    print("Senha incorreta.")
    senha = input("Digite sua senha: ")

print("Senha correta!")"""

#SAIR WHILE

"""while True:
    user_input = input("Digite 'sair' se quiser sair. ")
    if user_input == sair:
        break"""

#DIFERENTE DE ZERO E SOMA DOS DIGITADOS

"""number= int(input("Digite um numero:"))
soma = 0

while number != 0:
    print(number)
    soma += number
    number = int(input("Digite um numero:"))
    if number == 0:
        print(soma)
        print("Programa encerrado")
"""

#INTEIROS DIFERENTES DE ZERO E IMPRIME O MAIOR

"""number= int(input("Digite um numero:"))
maior = 0

while number != 0:
    number = int(input("Digite um numero:"))
    if number > maior:
        maior = number

print(maior)
"""

#CAIXA ELETRONICO BASICO(CONSULTA DE SALDO, DEPOSITO, SAQUE e SAIR DO PROGRAMA)

"""continuar = True
opc = 1
saldo = 0.0

while not continuar:
    print("1 -  Consulta")
    print("2 -  Deposito")
    print("3 -  Saque")
    print("4 -  Sair")

if opc == 0 or opc > 4:
    print("Digite uma opcao valida!")
elif opc == 1:
    print(saldo)
    
elif opc == 2:
    deposito = float(input("Digite o valor a ser depositado: "))
    saldo += deposito
"""


