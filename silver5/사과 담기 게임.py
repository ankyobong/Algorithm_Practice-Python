# https://www.acmicpc.net/problem/2828
n, m = map(int, input().split())
now = 0
basket = [0 for i in range(n)]
for i in range(m):
    basket[i] = 1
result = 0
for i in range(int(input())):
    j = int(input())
    if basket[j-1] == 1:
        continue
    while True:
        if now < j:
            basket[now] = 0
            basket[now+m] = 1
            now += 1
        else:
            basket[now+m-1] = 0
            basket[now-1] = 1
            now -= 1
        result += 1
        if basket[j-1] == 1:
            break
print(result)
