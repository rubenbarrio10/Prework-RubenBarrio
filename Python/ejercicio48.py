'''Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.'''


def contar_letras_y_digitos(cadena):
    num_letras = 0
    num_digitos = 0

    for caracter in cadena:
        if caracter.isalpha():
            num_letras += 1
        elif caracter.isdigit():
            num_digitos += 1

    return num_letras, num_digitos


texto = 'Buenosdías04102023'
letras, digitos = contar_letras_y_digitos(texto)

print(f'Número de letras: {letras}')
print(f'Número de dígitos: {digitos}')
