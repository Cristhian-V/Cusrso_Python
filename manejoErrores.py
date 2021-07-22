from typing import ValuesView


def divisors(num):
    divisors = []
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 1:
                divisors.append(i)
        return divisors
    else:
        raise TypeError
        

def run():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    print("Terminó mi programa")


if __name__ == '__main__':
    try:
        run()
    except ValueError:
        print("Solo se pueden ingresar numeros!!")
    except TypeError:
        print("debe ingresar un numero positivo")