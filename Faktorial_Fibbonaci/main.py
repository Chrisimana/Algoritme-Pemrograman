def faktorial(n):
    if n < 2:
        return 1
    else:
        return n * faktorial(n - 1)


def fib(n):
    if (n > 1):
        return fib(n - 1) + fib(n - 2)
    else:
        return n

print(faktorial(10))
print(faktorial(5))
print(faktorial(2))

print(fib(11))
print(fib(5))
print(fib(1))
