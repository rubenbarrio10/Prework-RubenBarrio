'''Define una función que reciba una lista de números y retorne la suma acumulada de los números'''


def suma_acumulada(lista):
    suma = 0
    suma_acumulada = []

    for numero in lista:
        suma += numero
        suma_acumulada.append(suma)
    return suma_acumulada


mi_lista = [1, 2, 3, 4, 5]
acumulado = suma_acumulada(mi_lista)

print(f'Lista original: {mi_lista}')
print(f'Suma acumulada: {acumulado}')
