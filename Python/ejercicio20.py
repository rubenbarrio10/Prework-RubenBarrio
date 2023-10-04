'''Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.'''


def sumar_digitos(numero):
    suma = 0  # Inicializamos la suma en 0
    # Convertimos el número en una cadena para iterar sobre sus dígitos
    numero_str = str(numero)

    for i in numero_str:  # i corresponde a los diferentes dígitos y empezará por el primero
        suma += int(i)  # Convertimos el dígito en un entero y lo sumamos
    return suma


numero = int(input('Ingrese un número: '))
resultado = sumar_digitos(numero)
print(f"La suma de los dígitos del número {numero} es {resultado}")
