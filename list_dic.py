#Lista en dicionarios, y diccionarios en listas
import random


def run():
    my_list = [1,"hello", True, 4.5]
    my_dic = {
        "firtname": "cristhian",
        "lastname": "Vargas",
        "edad": 33
        }
    
    super_list=[
        {"firtname":"Cristhian","lastname":"Vargas", "edad":34},
        {"firtname":"Samuel","lastname":"Vargas", "edad":30},
        {"firtname":"pancracio","lastname":"edmund", "edad":105}    
    ]

    super_dic={
        "numEnteros":[1,2,3,4,5,6,7,8,9],
        "numDecimales":[1.1,1.2,4.5,3.6,0.8,0.5,12.41],
        "numNegativos":[-1,-2,-3,-4,-5,-6,-7,-8,-9]
    }

    for llave, valor in super_dic.items():
        print(f"{llave} - {valor}")
        
    for item in super_list:
        for llave, valor in item.items():
            print(f"{llave} - {valor}")


def numCuadrados():
    listNum=[]
    for numero in range(100):
        listNum.append(random.randrange(100))
    
    print(listNum)

    for num in range(10):
        print(f"numero {num+1} {listNum[num]**2}")

#solo guardo los numeros que no son divisibles entre 3
def practica():
    listNum=[]
    for i in range(1,101):
        if i%3 != 0:
            listNum.append(i**2)
    
    print(listNum)

#list_comprehensions
def listComh():
    listNum = [i for i in range(1,100001) if (i % 4 == 0) and (i % 6 == 0) and (i % 9 == 0)]
    print(listNum)

def prectica1():
    myDic = {}
    for i in range(1,101):
        if i % 3 != 0:
            myDic[i] = i**3

    print(myDic)

#Dict_comprehensions
def dictComh():
    dictNum = {i:i**0.5 for i in range(1,1001)}
    print(dictNum)

if __name__ == "__main__":
    dictComh()