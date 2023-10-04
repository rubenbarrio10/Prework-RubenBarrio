'''Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.'''


def lista_en_orden_inverso(lista):
    lista_inversa = []
    for i in reversed(lista):
        lista_inversa.append(i)
    return lista_inversa


mi_lista = [1, 2, 3, 4, 5]
lista_inversa = lista_en_orden_inverso(mi_lista)

print(f'Lista original: {mi_lista}')
print(f'Lista en orden inverso: {lista_inversa}')
