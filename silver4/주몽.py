# https://www.acmicpc.net/problem/1940
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
numbers = set(map(int, sys.stdin.readline().split()))
a = sorted(numbers)
b = sorted(numbers, reverse=True)
result = 0
while a:
    for i in b:
        if a[0] == i:
            b.remove(i)
            a.remove(i)
            break
        elif a[0] + i >= m:
            result += 1
            b.remove(i)
            a.remove(i)
            break
    a.pop(0)

print(result)
