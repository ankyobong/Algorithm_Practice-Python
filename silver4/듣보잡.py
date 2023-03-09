# https://www.acmicpc.net/problem/1764
n, m = map(int, input().split())
a = list()
b = list()
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())
# result = sorted(set(a).intersection(b))
result = sorted(set(a) & set(b))
print(len(result))
print(*result, sep='\n')
