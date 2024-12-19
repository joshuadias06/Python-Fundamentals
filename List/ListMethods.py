numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = [ "Joshua", "Queren", "Davi", "Sophia", "Rebeca"]
sobrenomes = ["Dias", "Elizama", "Dias"]

numeros.reverse()
print(numeros)
numeros.sort()
print(numeros)
print(numeros.count(1))
print(numeros.index(1))

try:
    indice_nao_existe = numeros.index(100)
    print(numeros[indice_nao_existe])

except ValueError:
    print("Valor nao encontrado!")
