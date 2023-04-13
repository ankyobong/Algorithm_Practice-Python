# https://www.acmicpc.net/problem/2960
n, k = map(int, input().split())

era = [i for i in range(2, n+1)]

cnt = 0
result = 0
while True:
    p = min(era)
    r = 1
    while p*r < n+1:
        if p*r in era:
            era.remove(p*r)
            cnt += 1
        if cnt == k:
            result = p*r
            break
        else:
            r += 1
    if result != 0:
        break

print(result)
