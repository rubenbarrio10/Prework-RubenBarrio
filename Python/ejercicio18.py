'''Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.'''
# Función


def contar_digitos(numero):
    # Convierte el número en una cadena
    numero_str = str(numero)
    # Cuenta la cantidad de caracteres en la cadena
    cantidad_de_digitos = len(numero_str)

    print(f'La cantidad de dígitos es: {cantidad_de_digitos}')


# Ingreso de los datos
n = int(input('Ingrese un número: '))
contar_digitos(n)
