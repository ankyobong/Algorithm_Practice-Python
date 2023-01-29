# https://www.acmicpc.net/problem/1059
s_len = int(input())
s = [*map(int, input().split())]
n = int(input())
s.sort()
result = 0
if n in s:
    print(0)
    exit(0)
for i in range(s_len):
    if s[i] < n < s[i+1]:
        a = s[i]+1
        b = s[i+1]
        break
for i in range(a, b):
    for j in range(i+1, b):
        if j >= n >= i:
            result += 1
print(result)
