'''Dada una lista de números, crea una función que devuelva el número máximo de la lista.'''


def maximo(lista):
    if not lista:
        return None
    # m es igual al primer elemento de la lista de números ingresados
    m = lista[0]
    # Evaluación de los elementos mediante el bucle for
    for n in lista:
        if n > m:
            m = n
    return m


# Ingreso de datos
a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
c = int(input('Ingrese el tercer número: '))

# Envía los datos a la función y guarda el valor máximo en d
d = maximo([a, b, c])
print(f'El número mayor de la lista es: {d}')
