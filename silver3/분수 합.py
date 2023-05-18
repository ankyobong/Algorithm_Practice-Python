# https://www.acmicpc.net/problem/1735
from math import gcd
a, b = map(int, input().split())
c, d = map(int, input().split())

x, y = 0, 0
if b == d:
    x = a + c
    y = b + d
else:
    x = (a*d) + (c*b)
    y = b * d

print(int(x/gcd(x, y)), int(y/gcd(x, y)))
