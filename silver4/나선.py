# https://www.acmicpc.net/problem/1491
# 끝점으로 계속 이동
n, m = map(int, input().split())
x, y = -1, 0
p = 1

while True:
    x += n * p
    m -= 1
    if m == 0:
        break
    y += m * p
    n -= 1
    if n == 0:
        break
    p *= -1

print(x, y)
