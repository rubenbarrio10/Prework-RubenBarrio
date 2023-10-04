'''Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.'''


def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos
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


def numeros_primos(n):
    primos = []
    i = 2

    while len(primos) < n:
        if es_primo(i):
            primos.append(i)
        i += 1
    return primos


n = 10
primos = numeros_primos(n)

print(f'Los {n} primeros números primos son: {primos}')
