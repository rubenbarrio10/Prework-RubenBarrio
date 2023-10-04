'''Define una función que tome una lista de números y retorne el númer o más grande de la lista.'''


def numero_mas_grande(lista):
    if not lista:
        return None  # Retorna None si la lista está vacía
    return max(lista)


mi_lista = [5, 2, 9, 1, 7, 3, 8]
maximo = numero_mas_grande(mi_lista)

print(f'El número más grande en la lista es: {maximo}')
