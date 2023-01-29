# https://www.acmicpc.net/problem/1059
s_len = int(input())
s = [*map(int, input().split())]
n = int(input())
s.sort()
result = 0
for i in range(s_len):
    if s[i] < n < s[i+1]:
        a = s[i]
        b = s[i+1]
        break
for i in range(a+1, b):
    