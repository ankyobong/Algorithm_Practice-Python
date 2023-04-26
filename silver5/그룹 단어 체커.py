# https://www.acmicpc.net/problem/1316
import sys

n = int(input())
for i in range(n):
    a = sys.stdin.readline().rstrip()
    b = [a[0]]
    for i in list(a):
        if b[-1] == i:
            b.append(i)
            continue
        elif i in b:
            n -= 1
            break
        b.append(i)

print(n)
