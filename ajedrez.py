def tableroAjedrez():
    tableroinicial = ""
    tableroDic = {
        "a1":'♜\t', "a2":'♞\t', "a3":'♝\t', "a4":'♛\t', "a5":'♚\t', "a6":'♝\t',"a7":'♞\t',"a8":'♜\n',
        "b1":'♟\t', "b2":'♟\t', "b3":'♟\t', "b4":'♟\t', "b5":'♟\t', "b6":'♟\t', "b7":'♟\t', "b8":'♟\n',
        "c1":'\t', "c2":'\t', "c3":'\t', "c4":'\t', "c5":'\t', "c6":'\t', "c7":'\t', "c8":'\n',
        "d1":'\t', "d2":'\t', "d3":'\t', "d4":'\t', "d5":'\t', "d6":'\t', "d7":'\t', "d8":'\n',
        "e1":'\t', "e2":'\t', "e3":'\t', "e4":'\t', "e5":'\t', "e6":'\t', "e7":'\t', "e8":'\n',
        "f1":'\t', "f2":'\t', "f3":'\t', "f4":'\t', "f5":'\t', "f6":'\t', "f7":'\t', "f8":'\n',
        "g1":'♙\t', "g2":'♙\t', "g3":'♙\t', "g4":'♙\t', "g5":'♙\t', "g6":'♙\t', "g7":'♙\t', "g8":'♙\n',
        "h1":'♖\t', "h2":'♘\t', "h3":'♗\t', "h4":'♕\t', "h5":'♔\t', "h6":'♗\t', "h7":'♘\t', "h8":'♖\n' 
    }
    for key, value in tableroDic.items():
        tableroinicial += value
        

    return tableroinicial, tableroDic

def play(tablero_inicial, tableroDic):
    seguir = True
    contador = 0
    print(tablero_inicial)
    while seguir:
        jugadaIni = input("Que pieza deseas mover: ")
        jugadaDes = input("A donde deseas mover: ")

        tableroDic[jugadaDes] = tableroDic[jugadaIni]
        tableroDic[jugadaIni] = '\t'

        tableroDic = arreglaTablero(tableroDic)
        guardaJugada(tableroDic)

        Seguir = input("Quieres seguir Jugando (s/n): ")

        if Seguir == "n":
            seguir = False


def arreglaTablero(tableroDic):
    for key, value in tableroDic.items():
        if key[1] == "8":
            if len(value) > 1:
                pieza = tableroDic[key]
                pieza = pieza[0]
                tableroDic[key] = pieza + "\n"
    return tableroDic

def guardaJugada(tableroDic):
    Jugada = ""
    for key, value in tableroDic.items():
        Jugada += value
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f'{Jugada}')


def showMov(movimiento):
    contador = 0
    movs = ""
    with open("history.txt","r", encoding="utf-8") as f:
        for linea in f:
            if contador >= movimiento*8 and contador < (movimiento*8)+8:
                print (linea)
            contador += 1

if __name__ == "__main__":
    tablero_inicial, tableroDic = tableroAjedrez()
    play(tablero_inicial, tableroDic)
    movimiento = int(input("que movimiento quieres ver: "))
    showMov(movimiento)
    

