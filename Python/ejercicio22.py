'''Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.'''


def area_triangulo(altura, base):
    area = (altura * base) / 2
    return area


a = int(input('Ingrese el valor de la altura: '))
b = int(input('Ingrese el valor de la base: '))

resultado = area_triangulo(a, b)
print(f'El área del triángulo de altura {a} y base {b} es: {resultado}')
