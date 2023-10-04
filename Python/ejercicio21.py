'''Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.'''


def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a


def calcular_mcm(a, b):
    if a == 0 or b == 0:
        return 0  # El MCM de 0 y cualquier número es 0
    return abs(a * b) // calcular_mcd(a, b)


a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
mcm = calcular_mcm(a, b)
print(f"El MCM de {a} y {b} es {mcm}")
