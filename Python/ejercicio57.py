'''Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.'''


def cadena_mas_larga(lista_de_cadenas):
    cadena_mas_larga = lista_de_cadenas[0]

    for cadena in lista_de_cadenas:
        if len(cadena) > len(cadena_mas_larga):
            cadena_mas_larga = cadena
    return cadena_mas_larga


lista_cadenas = ["manzana", "plátano", "fresa", "melocotón"]
cadena_mas_grande = cadena_mas_larga(lista_cadenas)

print(f'La cadena más larga en la lista es: "{cadena_mas_grande}"')
