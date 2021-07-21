from functools import reduce

#Funciones anonimas (LAMBDA) Estas funciones no tiene un NOMBRE
def func_lambda ():
    palindromo = lambda palbra: palbra == palbra[::-1]
    palabra = input("ingresa un nombre: ")
    print(palindromo(palabra))

#Funciones de orden SUPERIOR
#estas funcines reciben una funcion como parametro para ejecutarla
#por convencion existen tres tipos de estas funciones
#FILTER()   MAP()    REDUCE()

##################  FILTER    ######################
#esta funcion Superior recibe una funcino y un elemento en este caso una lista
def func_Filter():
    myList = [1,2,3,4,5,6,7,8,9]
    odd = list(filter(lambda x: x%2 != 0,myList))
    print(odd)

##################  MAP    #########################
#esta funcion superior permite alterar un objero en este caso una lista y devolver el resultadop en una nueva lista
def func_Map():
    myList = [1,2,3,4,5,6,7,8,9]
    odd = list(map(lambda x: x**2,myList))  
    print(odd)

##################   REDUCE    ########################
#para esta funcion superior se tiene que importar REDUCE de "functools"
#lo que hace es operar con los valores de una lista es de cir puede +, -, *, / con todos los elelmento de la lista
def func_Reduce():
    myList = [1,2,3,4,5,6,7,8,9]
    odd = reduce(lambda a,b: a*b, myList)
    print(odd)

    
if __name__ == "__main__":
    func_Reduce()




