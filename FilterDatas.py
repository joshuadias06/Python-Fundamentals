numeros = [2, 5 ,8 ,10, 12, 15, 18, 20, 23, 25, 28]

numeros_impares= list(filter(lambda x: x % 2 != 0, numeros))

print("======================\n")
print(numeros_impares)
print("======================\n")

quadrados_impares = list(map(lambda x: x ** 2, numeros_impares))
print(quadrados_impares)
print("======================\n")
