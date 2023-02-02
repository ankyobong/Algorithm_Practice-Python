# https://www.acmicpc.net/problem/1158
n, k = map(int, input().split())
s = [i for i in range(1, n+1)]
result = []
t = 0
while s:
    t = (t+k-1) % len(s)
    result.append(str(s.pop(t)))

print("<"+', '.join(result)+">")
