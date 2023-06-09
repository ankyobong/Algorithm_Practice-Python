# https://www.acmicpc.net/problem/1120
a, b = input().split()

result = 50
for n in range(len(b)-len(a)+1):
    s = 0
    for i in range(len(a)):
        if a[i] != b[i+n]:
            s += 1
    if result > s:
        result = s

print(result)
