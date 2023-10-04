'''Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.'''


def contar_letras(palabra):
    contador = 0
    for letra in palabra:
        if letra.isalpha():  # Comprobar si cada carácter es una letra
            contador += 1
    return contador


palabra = input('Ingrese una palabra: ')
cantidad_letras = contar_letras(palabra)
print(f'La cantidad de letras en "{palabra}" es: {cantidad_letras}')
