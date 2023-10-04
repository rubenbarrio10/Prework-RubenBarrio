'''Define una función que tome una cadena y cuente el número de vocales en la cadena.'''


def contar_vocales(cadena):
    # Inicializamos un contador de vocales
    contador = 0
    # Definimos una cadena con todas las vocales en minúscula y mayúscula
    vocales = "aeiouAEIOU"

    # Iteramos a través de los caracteres de la cadena
    for i in cadena:
        # Verificamos si el carácter es una vocal
        if i in vocales:
            contador += 1
    return contador


texto = "Hola, ¿qué tal el fin de semana?"
numero_vocales = contar_vocales(texto)
print(f'El número de vocales en la cadena de texto es: {numero_vocales}')
