'''Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.'''


def imprimir_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b  # a toma el valor de b y b el valor de a + b


n = int(input('Ingrese la cantidad de números de Fibonacci que quiere imprimir: '))
imprimir_fibonacci(n)
