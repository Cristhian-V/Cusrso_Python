import datetime
import calendar

def ProgrecionGeometrica ():
    numeros = []
    resultado = 1
    for i in range(64):
        resultado += resultado 
        numeros.append(resultado)
    for i in numeros:
        print(i)

def bisiesto():
    fecha = int(input("ingresa un año: "))
    if fecha%4 == 0:
        print(f'el año {fecha} es bisiesto')
    else:
        print(f'el año {fecha} NO es bisiesto')

def imprimeFechaHora():
    fecha = datetime.datetime.now()
    print(f'fecha y hora en formato ISO {fecha.isoformat()}')
    print(f'{fecha.day}/{fecha.month}/{fecha.year}  {fecha.hour}:{fecha.minute}:{fecha.second}')

def calendario():
    c = calendar.TextCalendar(calendar.SUNDAY)
    c.prmonth(2020,11)

def tablaMultiplica():
    for i in range(1,11):
        for j in range(1,11):
            print(f'{i} * {j} = {i*j}')
        print('_'*40)


if __name__ == "__main__":
    tablaMultiplica()