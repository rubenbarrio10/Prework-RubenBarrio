'''Define una función que tome dos números y retorne su suma.'''


def suma(a, b):
    return a+b


a = int(input('Ingrese un número: '))
b = int(input('Ingrese otro número: '))

resultado = suma(a, b)
# Recordar que sin la f, no nos imprimirá lo que hay dentro de resultado
print(f'El resultado es: {resultado}')
