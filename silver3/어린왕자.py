# https://www.acmicpc.net/problem/1004
import sys
t = int(sys.stdin.readline())
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

for _ in range(t):
    n = int(sys.stdin.readline())
    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())