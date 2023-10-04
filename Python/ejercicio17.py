'''Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.'''


def calcular_factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial


numero = int(input('Ingrese un número:'))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")
