'''Dado un número, imprime si es par o impar.'''
# a = 14

a = int(input('Ingrese un número distinto de 0: '))

while a != 0:
    if a % 2 == 0:
        print('El número es PAR')
    else:
        print('El número es IMPAR')

    a = int(input('Ingrese otro número o pulse 0 para salir: '))

print('Fin del programa')
