# https://www.acmicpc.net/problem/1822
a, b = map(int, input().split())
a_l = [*map(int, input().split())]
b_l = [*map(int, input().split())]
result = sorted(set(a_l)-set(b_l))
print(len(result))
print(*result)