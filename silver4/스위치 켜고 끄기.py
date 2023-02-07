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
        lenght = min(n-num, num-1)
        ad = 0
        num -= 1
        if s_l[num] == 0:
            s_l[num] = 1
        else:
            s_l[num] = 0
        for i in range(lenght):
            i += 1
            if s_l[num-i] == s_l[num+i]:
                if s_l[num-i] == 0:
                    s_l[num-i] = 1
                    s_l[num+i] = 1
                else:
                    s_l[num-i] = 0
                    s_l[num+i] = 0
                continue
            break
for no, i in enumerate(s_l):
    if (no+1) % 20 == 0:
        print(i)
    else:
        print(i, end=' ')
