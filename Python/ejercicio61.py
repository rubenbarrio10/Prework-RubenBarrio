'''Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.'''


def contar_vocales(cadena):
    contador = 0
    # Definimos un conjunto de letras vocales para facilitar la verificación
    vocales = set("AEIOUaeiou")

    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador


texto = 'Hola, ¿cómo estás?'
cantidad_vocales = contar_vocales(texto)

print(f'Cantidad de vocales en la cadena: {cantidad_vocales}')
