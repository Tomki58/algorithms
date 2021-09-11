# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

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

def fibonacci_sum_fast(n):
    fibonacci_nums = [None] * (12*10 + 1)

    fibonacci_nums[0] = 0
    fibonacci_nums[1] = 1

    for i in range(2, len(fibonacci_nums)):
        fibonacci_nums[i] = (fibonacci_nums[i-1] + fibonacci_nums[i-2]) % 10

    fib_str = ",".join([str(num) for num in fibonacci_nums])

    period = list(map(int, get_fibonacci_period(fib_str).split(",")[:-1]))

    times = int(n / len(period))
    modulo = n % len(period)

    return (sum(period) * times) % 10 + sum(period[:modulo+1]) % 10

    

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))
