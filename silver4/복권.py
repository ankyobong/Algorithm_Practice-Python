# https://www.acmicpc.net/problem/1359
from itertools import combinations
n, m, k = map(int, input().split())
a = b = 0
for ca in combinations(range(n), m):
    for cb in combinations(range(n), m):
        a += 1
        if len(set(ca) & set(cb)) >= k:
            b += 1
print(b/a)
