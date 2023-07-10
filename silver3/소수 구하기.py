# https://www.acmicpc.net/problem/1929
import math

m, n = map(int, input().split())


def is_prime_num(num: int):
    arr = [True] * (num + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(num)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= num:
                arr[i*j] = False
                j += 1

    return arr


result = is_prime_num(n)
for i in range(len(result)-m):
    if result[m+i]:
        print(m+i)
