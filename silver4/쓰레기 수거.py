# https://www.acmicpc.net/problem/1680
t = int(input())
for _ in range(t):
    w, n = map(int, input().split())
    w_t = x_t = result = 0
    for i in range(n):
        x_i, w_i = map(int, input().split())
        w_t += x_i
        x_t += x_i
        if w_t >= w:
            result += x_i
            w_t = x_t = 0
    print(result)
