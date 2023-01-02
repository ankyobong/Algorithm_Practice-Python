# https://www.acmicpc.net/problem/2635
n = int(input())
s = 0
l_max = []

while True:
    a = [n, n-s]
    count = 0
    while True:
        next_n = a[-2]-a[-1]
        if next_n < 0:
            break
        a.append(next_n)
    if len(l_max) <= len(a):
        l_max = a
        s += 1
    else:
        break
print(len(l_max))
for i in l_max:
    print(i, end=' ')

