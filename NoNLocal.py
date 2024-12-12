print("\n--------------------------\n")
def funcao_externa():
     var_externa = "Eu sou externa"

     def func_interna():
         nonlocal var_externa
         print(var_externa)
         var_externa = "Eu fui modificada pela func interna"
         print(var_externa)

     func_interna()
     print(var_externa)
funcao_externa()