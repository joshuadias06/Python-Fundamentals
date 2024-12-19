lista = ["maca", "banana", "cereja", "damasco"]

#Funcao Lambda com sorted

pessoas = [("Joshua", 21),("Queren", 21),("Davi", 1),("Sophia", 1)]

pessoas_ordenadas= sorted(pessoas, key = lambda x: x[1])

print(pessoas_ordenadas)