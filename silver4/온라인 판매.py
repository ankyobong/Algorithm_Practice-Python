# https://www.acmicpc.net/problem/1246
n, m = map(int, input().split())
pi = []
for _ in range(m):
    pi.append(int(input()))
p = 0
max_p = 0
pi.sort()
for i in range(m):
    e = min(m-i, n)
    if max_p < pi[i] * e:
        max_p = pi[i] * e
        p = pi[i]
print(p, max_p)
