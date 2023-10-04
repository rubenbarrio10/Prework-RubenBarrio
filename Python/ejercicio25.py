'''Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.'''


def valor_absoluto_lista(lista):
    lista_absoluta = [abs(numero) for numero in lista]
    return lista_absoluta


a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
c = int(input('Ingrese el tercer número: '))

numeros = [a, b, c]
resultado = valor_absoluto_lista(numeros)
print(f'Lista original: {numeros}')
print(f'Lista con valor absoluto: {resultado}')
