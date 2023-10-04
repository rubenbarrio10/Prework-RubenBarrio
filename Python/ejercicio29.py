'''Define una función que tome un número y retorne una lista de sus divisores.'''


def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


numero = int(input('Ingrese un número: '))
lista_divisores = encontrar_divisores(numero)
print(f'Los divisores de {numero} son: {lista_divisores}')
