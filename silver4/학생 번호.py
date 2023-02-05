# https://www.acmicpc.net/problem/1235
s_l = []
for _ in range(int(input())):
    s_l.append(input())

k = 3
check = True
while check:
    s = []
    c = []
    for i in s_l:
        if i[-k:] in s:
            c.append(i)
            break
        s.append(i[-k:])
    if c:
        k += 1
        check = True
    else:
        print(k)
        break