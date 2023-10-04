'''Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.'''


def tabla_de_multiplicar(numero):
    tabla = {}
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        tabla[multiplicador] = resultado
    return tabla


n = 5
tabla = tabla_de_multiplicar(n)

print(f'Tabla de multiplicar del {n}:')
for multiplicador, resultado in tabla.items():
    print(f'{n} x {multiplicador} = {resultado}')
