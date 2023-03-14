# https://www.acmicpc.net/problem/1835
n = int(input())
result = [n]
for i in reversed(range(1, n)):
    result.append(result.pop(0))
    result = [i] + result
result = [result.pop(-1)] + result
print(*result)
