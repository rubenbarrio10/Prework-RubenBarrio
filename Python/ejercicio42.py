'''Define una función que tome un número y calcule su serie de Fibonacci.'''


def fibonacci(n):
    fibonacci_seq = [0, 1]

    while len(fibonacci_seq) < n:
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_num)
    return fibonacci_seq[:n]


n = 4
secuencia_fibonacci = fibonacci(n)

print(
    f'Serie de Fibonacci con los primeros {n} términos: {secuencia_fibonacci}')
