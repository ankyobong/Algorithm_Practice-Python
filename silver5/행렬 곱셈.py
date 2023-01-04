# https://www.acmicpc.net/problem/2740
n, m = map(int, input().split())
a = [[*map(int, input().split())]for _ in range(n)]
m, k = map(int, input().split())
b = [[*map(int, input().split())]for _ in range(m)]

c = [[0 for _ in range(k)] for _ in range(n)]

for sn in range(n):
    for sk in range(k):
        for sm in range(m):
            c[sn][sk] += a[sn][sm] * b[sm][sk]

for i in c:
    for j in i:
        print(j, end=' ')
    print()
