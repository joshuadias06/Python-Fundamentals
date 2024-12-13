def maiorMenor(lista):
    for item in lista:
        if item > lista[0]:
            maior = item

    for item in lista:
        if item < lista[0]:
            menor = item

    return maior, menor

lista = list(map(int, input("Digite os valores na lista separados por espaços: ").split()))
maior, menor = maiorMenor(lista)
print(maior, menor)