'''Dado un número, imprime si es positivo o negativo.'''
# a = 10
# En lugar de revisar un número dado, podemos pedir al usuario que lo ingrese
a = int(input('Ingrese un número: '))

# Con este bucle se consigue poder preguntar por diferentes números en lugar de iniciar el programa cada vez
while a != 0:
    if a > 0:
        print('El número es positivo')
    else:
        print('El número es negativo')
    a = int(input('Ingrese otro número o pulse 0 para salir: '))

print('Fin del programa')
