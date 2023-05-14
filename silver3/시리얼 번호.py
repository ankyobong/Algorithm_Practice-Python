# https://www.acmicpc.net/problem/1431
import re

n = int(input())
d = dict()
for _ in range(n):
    inp = input()
    if len(inp) in d:
        d[len(inp)][inp] = sum([int(i) for i in re.sub(f'[^1-9]', '', '145C')])
    else:
        d[len(inp)] = {inp: sum([int(i) for i in re.sub(f'[^1-9]', '', '145C')])}

for i in sorted(d.keys()):
    print(d[i])
