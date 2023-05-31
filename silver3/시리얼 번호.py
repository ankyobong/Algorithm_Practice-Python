# https://www.acmicpc.net/problem/1431
import re

n = int(input())
d = dict()

for _ in range(n):
    inp = input()
    if len(inp) in d:
        d[len(inp)][inp] = sum([int(i) for i in re.sub(f'[^1-9]', '', inp)])
    else:
        d[len(inp)] = {inp: sum([int(i) for i in re.sub(f'[^1-9]', '', inp)])}

for i in sorted(d.keys()):
    for j in sorted(sorted(d[i].items()), key=lambda x: x[1]):
        print(j[0])
