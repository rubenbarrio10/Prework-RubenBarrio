'''Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.'''


def cadena_invertida(cadena):
    palabras = cadena.split()  # Divide la cadena en palabras
    palabras_invertidas = palabras[::-1]  # Invierte el orden de las palabras
    # Une las palabras en una cadena
    cadena_invertida = ' '.join(palabras_invertidas)
    return cadena_invertida


texto = 'Buenos días, Madrid'
texto_invertido = cadena_invertida(texto)

print(f'Cadena original: "{texto}"')
print(f'Cadena invertida: "{texto_invertido}"')
