# https://www.acmicpc.net/problem/3049
import operator as op
from functools import reduce


def nc4(n: int):
    r = min(4, n-4)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


n = int(input())
if n == 3:
    print(0)
else:
    print(nc4(n))
