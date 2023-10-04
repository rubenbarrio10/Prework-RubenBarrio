'''Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.'''


def es_primo(numero):
    if numero <= 1:
        return False

    if numero <= 3:
        return True  # 2 y 3 son primos

    if numero % 2 == 0 or numero % 3 == 0:
        return False  # Los múltiplos de 2 y 3 no son primos

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False  # Si es divisible por algún número entre i y i+2, no es primo
        i += 6
    return True


n = 17
resultado = es_primo(n)

if resultado:
    print(f'{n} es un número primo.')
else:
    print(f'{n} no es un número primo.')
