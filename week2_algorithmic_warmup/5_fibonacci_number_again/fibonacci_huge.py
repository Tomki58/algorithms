# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_period(fib_string: str):
    """ Finds the period in the fibonacci modules row """

    m = 1
    candidate = ""

    while m <= len(fib_string) / 2:
        candidate = fib_string[:m]
        try:
            next_idx = fib_string.index(candidate, m, len(fib_string))
        except:
            pass

        if next_idx == m:
            return candidate

        m += 1

    return fib_string


def get_fibonacci_huge_fast(n, m):
    fib_numbers = [None] * (12*m + 1)
    fib_numbers[0] = 0
    fib_numbers[1] = 1

    for i in range(2, len(fib_numbers)):
        fib_numbers[i] = (fib_numbers[i-1] + fib_numbers[i-2]) % m

    fib_modulo_string = ",".join([str(num) for num in fib_numbers])
    fib_modulo_period = get_fibonacci_period(fib_modulo_string)
    fib_modulo_num = fib_modulo_period.split(",")[:-1]

    return (fib_modulo_num[n % len(fib_modulo_num)])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))
