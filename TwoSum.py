def TwoSum(vect, target):
    for i in range(len(vect)):
        for j in range(i +1 ,len(vect)):
            if vect[i] + vect[j] == target:
                return {vect[i], vect[j]}

    return {}

lista = [1, 6, 11 , -2, 9, 5]
target = 9
print(TwoSum(lista, target))