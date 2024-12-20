#List Comprehensions

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = [x**2 for x in range(10)]
print(quadrados)

quadrados =[]


#Tradicional
for x in range(10):
    quadrados.append(x**2)

print(quadrados)

quadrado_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrado_pares)

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
combinacoes = []

for x in a:
    for y in b:
        if x + y == 5:
            combinacoes.append((x , y))

print(combinacoes)
combinacoes = []

combinacoes = [(x,y) for x in a for y in b if x + y == 5]
print(combinacoes)


