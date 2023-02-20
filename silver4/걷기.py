# https://www.acmicpc.net/problem/1459
x, y, w, s = map(int, input().split())

result = list()
result.append((x+y)*w)
if (x + y) % 2 == 0:
    result.append(max(x, y)*s)
elif (x + y) % 2 == 1:
    result.append((max(x, y)-1)*s + w)
result.append((min(x, y) * s) + ((max(x, y) - min(x, y)) * w))

print(min(result))