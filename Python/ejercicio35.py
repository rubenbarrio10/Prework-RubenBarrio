'''Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.'''


def es_numero_perfecto(numero):
    if numero <= 0:
        return False

    suma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero


n = 6
resultado = es_numero_perfecto(n)
if resultado:
    print(f'{n} es un número perfecto')
else:
    print(f'{n} no es un número perfecto.')
