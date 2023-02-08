# https://www.acmicpc.net/problem/1246
n, m = map(int, input().split())
pi = []
for _ in range(m):
    pi.append(int(input()))
p = 0
max_p = 0
ps = sorted(pi, reverse=True)
for i in sorted(set(pi), reverse=True):
    t = 0
    for j in range(min(m, n)):
        if i <= ps[j]:
            t += i
            continue
        break
    if t > max_p:
        p = i
        max_p = t
        continue
    break

print(p, max_p)
