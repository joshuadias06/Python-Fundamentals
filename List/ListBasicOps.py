numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = [ "Joshua", "Queren", "Davi", "Sophia", "Rebeca"]
sobrenomes = ["Dias", "Elizama", "Dias"]

numeros.append(100)
print(numeros)
numeros.remove(100)
print(numeros)
numeros.insert(1, 100)
print(numeros)
numeros.pop(1)
print(numeros)
numeros.extend([100, 200, 300])
print(numeros)
numeros.remove(100)
numeros.remove(200)
numeros.remove(300)
print(numeros)
nomes.extend(sobrenomes)
print(nomes)
print("Joshua" in nomes)
print("Joshuaaa" in nomes)
