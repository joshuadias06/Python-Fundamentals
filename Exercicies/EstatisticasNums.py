def estatisticasMD1(*args):
    soma = sum(args)  # Calcula a soma diretamente
    media = soma / len(args)  # Calcula a média

    # Inicializa maior e menor como o primeiro elemento da lista
    maior = args[0]
    menor = args[0]

    # Percorre os elementos para determinar maior e menor
    for i in range(len(args)):
        if args[i] > maior:
            maior = args[i]
        if args[i] < menor:
            menor = args[i]

    return media, maior, menor


def estatisticasMD2(*args):
    return sum(args) / len(args), max(args), min(args)


numeros = list(map(int, input("Digite uma sequência de números separados por espaço: ").split()))

#media, maior, menor = estatisticasMD1(*numeros)
media, maior, menor = estatisticasMD2(*numeros)

print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
