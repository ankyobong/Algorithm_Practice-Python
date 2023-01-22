# https://www.acmicpc.net/problem/1021
from collections import deque

n, m = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
pick = list(map(int, input().split()))
cnt = 0

for i in pick:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q) // 2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1
print(cnt)