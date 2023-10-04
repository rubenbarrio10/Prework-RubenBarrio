'''Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.'''


def palabras_mas_largas_que_n(lista_palabras, n):
    palabras_largas = []
    for i in lista_palabras:
        if len(i) > n:
            # Utilizamos append para agragar las palabras que cumplen a la lista
            palabras_largas.append(i)
    return palabras_largas


lista_palabras = ["manzana", "plátano", "kiwi", "sandía", "pera"]
n = 4
palabras_largas = palabras_mas_largas_que_n(lista_palabras, n)

print(f'Palabras más largas que {n} caracteres: {palabras_largas}')
