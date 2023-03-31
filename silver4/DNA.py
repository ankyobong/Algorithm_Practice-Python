# https://www.acmicpc.net/problem/1969
import sys

n, m = map(int, sys.stdin.readline().split())

dna_list = list()
result = ''
cnt = 0

for _ in range(n):
    dna_list.append(sys.stdin.readline().strip())

for i in range(m):
    dna = {'A': 0,
           'C': 0,
           'G': 0,
           'T': 0}
    for j in range(n):
        dna[dna_list[j][i]] += 1
    a = max(dna.values())
    for d in dna.keys():
        if dna[d] == a:
            result += d
            cnt += n-a
            break

print(result)
print(cnt)
