'''Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.'''


def es_par(numero):
    return numero % 2 == 0


# Pedimos un valor y lo guardamos en la n
n = int(input('Ingrese un número para comprobar si es par o impar: '))

# Enviamos a la función el valor ingresado para que nos devuelva True o False
if es_par(n):
    print('Es un número par')
else:
    print('Es un número impar')
