# https://www.acmicpc.net/problem/1788
n = int(input())


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def min_fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return min_fib(n + 1) - min_fib(n + 2)


if n > 0:
    print(1)
    print(abs(fib(n)))
elif n == 0:
    print(0)
else:
    print(-1)
    print(abs(fib(abs(n))))
