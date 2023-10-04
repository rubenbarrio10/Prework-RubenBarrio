'''Define una función que reciba una lista de números y retorne la suma de ellos.'''


def suma(lista):  # Definimos la función
    return sum(lista)


# Pedimos los valores al usuario
a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
c = int(input('Ingrese el tercer número: '))
# Pasamos los valores a la función y guardamos el resultado
resultado = suma([a, b, c])

print(f'El resultado es: {resultado}')
