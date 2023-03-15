# https://www.acmicpc.net/problem/1835
n = int(input())
result = [n]
for i in reversed(range(1, n)):
    result.append(i)
    for j in range(i):
        result.append(result.pop(0))
# result = [result.pop(-1)] + result
print(*reversed(result))
