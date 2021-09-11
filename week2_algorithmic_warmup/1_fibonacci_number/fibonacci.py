def calc_fib_fast(n):
    """ Fast calculation of fibonacci number """
    fibonacci = [0 for i in range(n + 1)]
    fibonacci[1] = 1

    for i in range(2, n + 1):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    return fibonacci[n]


n = int(input())
print(calc_fib_fast(n))
