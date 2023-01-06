# https://www.acmicpc.net/problem/2890
import re
le = [0 for _ in range(10)]
r, c = map(int, input().split())

for i in range(r):
    l = input()
    idx = re.sub(r'[^1-9]', '', l)
    if idx:
        le[int(idx[0])] = c - l.rfind(idx[0]) - 1

rank = list(set(sorted(le)))
result = ''.join([str(i) for i in le])
for n, i in enumerate(rank):
    result = result.replace(str(i), str(n))
for i in result[1:]:
    print(i)
