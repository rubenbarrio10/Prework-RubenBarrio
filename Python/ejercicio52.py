'''Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.'''


def contar_apariciones_caracteres(cadena):
    apariciones = {}
    for caracter in cadena:
        if caracter in apariciones:
            apariciones[caracter] += 1
        else:
            apariciones[caracter] = 1
    return apariciones


texto = 'Buenos días, Madrid'
resultado = contar_apariciones_caracteres(texto)

print('Apariciones de caracteres:')
for caracter, cantidad in resultado.items():
    print(f"'{caracter}': {cantidad}")
