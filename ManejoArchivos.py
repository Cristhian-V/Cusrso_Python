def read():
    listLineas=[]
    with open("./archivos/arch.txt","r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea != "\n":
                listLineas.append(linea)
    return listLineas

#en este codigo se esta escriviendo un archivo por lo tanto si ya existe el archivo es borrado 
#y creado otro en sulugar con el nuvo contenido
#el modo "w" sobre escribe "a" adiciona nuevas lineas
def write():
    nombres = ["cristhian", "facundo", "yery", "Margarita", "Laura"]
    with open("./archivos/names.txt", "w", encoding= "utf-8") as f:
        for nombre in nombres:
            nombre = nombre + " \n"
            f.write(nombre )


if __name__ == "__main__":
    write()