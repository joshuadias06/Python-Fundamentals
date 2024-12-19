quadrados_impares = [x ** 2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

#Outra forma de fazer:

"""for x in range(10):
    if x % 2 != 0:
        quadrados_impares.append(x ** 2)
        print(quadrados_impares)"""