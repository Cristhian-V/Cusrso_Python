import turtle

def ventana(NroPuntas):
    gradosEstrella = calculaGrado(NroPuntas)
    turtle.showturtle()
    turtle.goto(-250,0)
    for i in range(NroPuntas):
        turtle.forward(500)
        turtle.left(gradosEstrella)
    
    input("sssssssss")

def calculaGrado(NroPuntas):
    resultado = -(180/ NroPuntas) + 180
    return resultado

if __name__ == "__main__":
    NroPuntas = int(input('ingrese el numero de puntas de la estrella: '))
    ventana(NroPuntas)

