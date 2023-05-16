# https://www.acmicpc.net/problem/1072
x, y = map(int, input().split())
z = y/x*100
zn = y/x*100
n = 0
while int(z) == int(zn):
    n += 1
    if zn == (y+n) / (x+n) * 100:
        n = -1
        break
    zn = (y+n) / (x+n) * 100

print(n)
