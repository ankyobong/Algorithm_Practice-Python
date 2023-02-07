# https://www.acmicpc.net/problem/1244
n = int(input())
s_l = [*map(int, input().split())]
for _ in range(int(input())):
    s, num = map(int, (input().split()))
    if s == 1:
        for i in range(1, (n//num)+1):
            t = (i*num) - 1
            if s_l[t] == 0:
                s_l[t] = 1
            else:
                s_l[t] = 0
    else:
        print(s)
