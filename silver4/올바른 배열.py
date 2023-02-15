# https://www.acmicpc.net/problem/1337
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
result = []
for i in l:
    t = 0
    for j in range(i, i+5):
        if j not in l:
            t += 1
    result.append(t)

print(min(result))
