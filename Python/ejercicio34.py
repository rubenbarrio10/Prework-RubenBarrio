'''Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.'''


def contar_letras_mayusculas_y_minusculas(cadena):
    mayusculas = 0
    minusculas = 0

    # Iteramos a través de los caracteres de la cadena
    for caracter in cadena:
        # Verificamos si el carácter es una letra mayúscula
        if caracter.isupper():
            mayusculas += 1
        # Verificamos si el carácter es una letra minúscula
        elif caracter.islower():
            minusculas += 1
    return mayusculas, minusculas


texto = "Comprobación del número de mayúsculas y minúsculas en esta frase"
mayusculas, minusculas = contar_letras_mayusculas_y_minusculas(texto)

print(f'Cantidad de letras mayúsculas: {mayusculas}')
print(f'Cantidad de letras minúsculas: {minusculas}')
