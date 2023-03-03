# https://www.acmicpc.net/problem/1680
t = int(input())
for _ in range(t):
    w, n = map(int, input().split())
    w_t = x_t = result = 0
    for i in range(n):
        x_i, w_i = map(int, input().split())
        result += x_i - x_t
        x_t = x_i
        w_t += w_i
        if w_t == w and i != n -1:
            result += 2 * x_i
            w_t = 0
        elif w_t > w:
            result += 2 * x_i
            w_t = w_i
    print(result+x_i)
