# https://www.acmicpc.net/problem/2890
import re
le = [-1 for _ in range(9)]
r, c = map(int, input().split())

for _ in range(r):
    idx = re.split('[1-9]{2}', input())
    if idx[0].count('.') != (c - 2):
        le[int(idx[1][0])-1] = ((c-5) - idx[0].count('.'))

d = {}
rank = 1
for num in sorted(le):
    if num not in d:
        d[num] = rank
        rank += 1
result = [d[i] for i in le]
for i in result:
    print(i)
