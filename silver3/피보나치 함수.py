# https://www.acmicpc.net/problem/1003
def fibonacci(n: int):
    if n == 0:
        print("0")
        return 0
    elif n == 1:
        print("1")
        return 1
    # else:
    #     n = fibonacci(n‐1) + fibonacci(n‐2)
