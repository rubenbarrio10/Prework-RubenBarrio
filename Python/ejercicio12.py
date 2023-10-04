'''Define una función que tome un número y retorne su factorial.'''


def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)


a = int(input('Ingrese un número: '))

print(factorial(a))
