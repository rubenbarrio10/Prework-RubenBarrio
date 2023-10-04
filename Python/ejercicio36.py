'''Define una función que reciba un número y retorne su representación en binario.'''


def decimal_a_binario(numero):
    return bin(numero)


n = 10
representacion_binaria = decimal_a_binario(n)
print(f'La representación binaria de {n} es: {representacion_binaria}')
