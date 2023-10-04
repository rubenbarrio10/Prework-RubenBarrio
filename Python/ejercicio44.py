'''Define una función que reciba un número y retorne la suma de sus dí gitos al cubo.'''


def suma_digitos_al_cubo(numero):
    # Convertimos el número en una cadena para iterar a través de sus dígitos
    numero_str = str(numero)
    suma_cubos = 0

    for digito in numero_str:
        digito_int = int(digito)
        cubo = digito_int ** 3
        suma_cubos += cubo
    return suma_cubos


n = 12345
resultado = suma_digitos_al_cubo(n)

print(f'Suma de los cubos de los dígitos de {n}: {resultado}')
