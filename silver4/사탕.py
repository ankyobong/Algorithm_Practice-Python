# https://www.acmicpc.net/problem/1812
n = int(input())
canddy = []
sum = 0
for i in range(n):
    a = int(input())
    canddy.append(a)
    sum += a
sum //= 2
for i in range(n):
    num = 0
    for j in range(1, n, 2):
        num += canddy[(i + j) % n]
    print(sum - num)
