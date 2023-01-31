# https://www.acmicpc.net/problem/1065
n = int(input())
result = 0
for i in range(1, n+1):
    if i < 100:
        result += 1
        continue
    if (i % 10//1) - (i % 100//10) == (i % 100//10) - (i % 1000//100):
        result += 1
if n == 1000:
    result -= 1
print(result)
