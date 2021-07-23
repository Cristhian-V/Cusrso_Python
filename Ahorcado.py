from math import trunc
import random

def run():
    listLeter = []
    wordhidden = selecWord()
    wordhidden = wordhidden.upper()
    show(wordhidden,listLeter)
    ganaste = False

    while not ganaste :
        letra = input("ingresa una letra: ").upper()
        listLeter.append(letra)
        ganaste = show(wordhidden,listLeter)


def selecWord():
    listWord = []
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            listWord.append(palabra)
    return listWord[random.randrange(len(listWord))]


def show(wordhidden, listleter):
    dictshow = {i:"_" for i in wordhidden if i != "\n"}
    for key,value in  dictshow.items():
        for leter in listleter:
            if leter == key:
                dictshow[key]=leter
    listshow = [j for i,j in dictshow.items()]
    contador = 0
    for i in listshow:
        if i == "_":
           contador += 1
    
    if contador == 0:
        return True
            
    print(listshow)
    


if __name__ == "__main__":
    run()