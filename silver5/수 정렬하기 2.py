# https://www.acmicpc.net/problem/2751
import sys
result = [int(sys.stdin.readline()) for _ in range(int(input()))]
result.sort()
for i in result:
    print(i)

