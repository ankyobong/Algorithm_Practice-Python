# https://www.acmicpc.net/problem/1269
la, lb = map(int, input().split())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

print(*set(a) ^ set(b))
