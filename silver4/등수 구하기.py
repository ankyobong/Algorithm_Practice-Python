# https://www.acmicpc.net/problem/1205
n, new, p = map(int, input().split())

if n == 0:
    print(1)
else:
    ranking = [*map(int, input().split())]
    if n == p and ranking[-1] >= new:
        print(-1)
    else:
        result = n + 1
        for i in range(n):
            if ranking[i] <= new:
                result = i + 1
                break
        print(result)
