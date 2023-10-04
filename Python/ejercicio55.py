'''Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.'''


def suma_cuadrados_numeros_pares(numero):
    if numero < 2:
        return 0  # Retorna 0 si el número es menor que 2

    suma = 0
    # start = 2 // stop = número dado + 1 // step = 2 para obtener solo los números pares
    for i in range(2, numero + 1, 2):
        suma += i**2
    return suma


n = 6
resultado = suma_cuadrados_numeros_pares(n)

print(
    f'Suma de los cuadrados de números pares menores o iguales a {n}: {resultado}')
