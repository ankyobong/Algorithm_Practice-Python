# https://www.acmicpc.net/problem/1059
s_len = int(input())
s = [*map(int, input().split())]
n = int(input())
s.sort()

if n in s:
    print(0)
else:
    result = 0
    a, b = 0, 0

    for i in s:
        if i < n:
            a = i
        elif i > n and b == 0:
            b = i
    a += 1
    b -= 1

    result = (b-n) + (n-a)*(b-n+1)
    print(result)