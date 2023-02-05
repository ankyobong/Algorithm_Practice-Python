# https://www.acmicpc.net/problem/1235
s_l = []

for _ in range(int(input())):
    s_l.append(input()[::-1])

for k in range(1, len(s_l[0])+1):
    temp = [num[:k] for num in s_l]
    if len(temp) == len(set(temp)):
        print(k)
        break
