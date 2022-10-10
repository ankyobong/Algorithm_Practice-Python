# https://www.acmicpc.net/problem/1312

a, b, n = map(int, input().split())
a %= b
for i in range(n-1):
    a = (a*10) % b
print((a*10)//b)

# 파이썬 연산자는 최대로 보여주는 범위가 있다 따라서 직접 계산해야함...
