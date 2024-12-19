def sumList(list):
    soma = 0
    for item in list:
        soma += item

    return soma

lista = list(map(int, input("Digite os numeros para ser somados: ").split()))
list = [1, 2, 3, 4, 5]
result = sumList(list)

print(result)
print(sumList(lista))