'''Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.'''


def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a


numero1 = int(input('Ingresa un número: '))
numero2 = int(input('Ingresa otro número: '))
mcd = calcular_mcd(numero1, numero2)
print(f'El MCD de {numero1} y {numero2} es: {mcd}')
