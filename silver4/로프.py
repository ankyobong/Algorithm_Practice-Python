# https://www.acmicpc.net/problem/2217
import sys

n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]

ropes.sort(reverse=True)
result = []

for i in range(n):
    result.append(ropes[i]*(i+1))

print(max(result))
