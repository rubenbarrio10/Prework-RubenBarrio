'''Define una función que reciba una lista de números y retorne el promedio de los números en la lista.'''


def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio


mi_lista = [1, 2, 3, 4, 5]
promedio = calcular_promedio(mi_lista)

print(f'Promedio de la lista: {promedio}')
