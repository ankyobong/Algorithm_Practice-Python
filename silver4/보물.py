# https://www.acmicpc.net/problem/1026
n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

a.sort()
b.sort(reverse=True)
result = 0
for i in range(n):
    result += a[i]*b[i]
print(result)
