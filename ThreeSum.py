def ThreeSum(vect, target):
    for i in range(len(vect)):
        for j in range(i +1 ,len(vect)):
            for k in range(j+1,len(vect)):
                if vect[i] + vect[j] + vect[k] == target:
                    return {vect[i], vect[j], vect[k]}

    return {}

lista = [1, 6, 11 , -2, 9, 5]
target = 9
print(ThreeSum(lista, target))