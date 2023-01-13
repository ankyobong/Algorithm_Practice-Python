# https://www.acmicpc.net/problem/3135
import sys


A, B = map(int, input().split())
N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

temp = abs(A-B)
min_cha = 242424242424
for i in range(N):
    if abs(data[i] - B) < min_cha:
        min_cha = abs(data[i] - B)
        idx = i
if temp <= min_cha:
    print(abs(A-B))
else:
    print(abs(B - data[idx]) + 1)
