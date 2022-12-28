# https://www.acmicpc.net/problem/2422
n, m = map(int, input().split())
ice_l = [[True for _ in range(n)]for _ in range(n)]
for i in range(m):
    a, b = ((lambda x: x-1)(i) for i in (map(int, input().split())))
    ice_l[a][b] = ice_l[b][a] = False

result = 0
for one in range(n):
    for two in range(one+1, n):
        for three in range(two+1, n):
            if ice_l[one][two] and ice_l[one][three] and ice_l[two][three]:
                result += 1
print(result)
