'''Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.'''


def segundo_numero_mas_grande(lista):
    lista_ordenada = sorted(lista, reverse=True)
    segundo_mas_grande = lista_ordenada[1]
    return segundo_mas_grande


mi_lista = [5, 2, 9, 1, 7, 3, 8]
segundo_maximo = segundo_numero_mas_grande(mi_lista)

print(f'El segundo número más grande en la lista es: {segundo_maximo}')
