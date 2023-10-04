'''Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''


def es_palindromo(cadena):
    # Eliminamos espacios y convertimos a minúsculas para simplificar la comparación
    cadena = cadena.replace(" ", "").lower()
    # Comparamos la cadena original con su versión invertida
    return cadena == cadena[::-1]


texto = 'La casa de Juan está en llamas'
resultado = es_palindromo(texto)

if resultado:
    print(f'"{texto}" es un palíndromo')
else:
    print(f'"{texto}" no es un palíndromo')
