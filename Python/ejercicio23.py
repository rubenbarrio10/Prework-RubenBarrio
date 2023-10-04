'''Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.'''


def verificado_numero(valor):
    if valor == 0:
        print('El número introducido es 0')
    elif valor > 0:
        print('El número es positivo')
    else:
        print('El número es negativo')


# Bucle para pedir el número continuamente
while True:
    a = int(input('Ingrese un número o pulse 0 para salir: '))
    if a == 0:
        print('El número introducido es 0')
        print('Fin del programa')
        break
    # Tiene que estar en el bucle para llamar a la función cada vez que se inserte un número
    verificado_numero(a)
