'''Define una función que tome un número y determine si es primo.'''


def primo(n):

    if n < 2:
        return False
# n es el valor ingresado por el usuario e i los valores en ese rango
# Si n fuese 5, i tomaría los valores 2, 3 y 4
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


resultado = primo(5)
print(f'¿El número es primo? {resultado}')
