# https://www.acmicpc.net/problem/1940
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
numbers = set(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)
start, end = 0, n-1
result = 0
while start < end:
    if numbers[start] + numbers[end] == m:
        result += 1
        start += 1
        end -= 1
    elif numbers[start] + numbers[end] < m:
        start += 1
    else:
        end -= 1

print(result)
