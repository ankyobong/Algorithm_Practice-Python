# https://www.acmicpc.net/problem/1358
w, h, x, y, p = map(int, input().split())
result = 0
l_c = (x, y+(h/2))
r_c = (x+w, y+(h/2))
for _ in range(p):
    i, j = map(int, input().split())
    if x-(h/2) <= i <= x+w+(h/2) and y <= j <= y+h:
        if x <= i <= x+w:
            result += 1
        elif ((l_c[0]-i)**2 + (l_c[1]-j)**2)**0.5 <= h/2:
            result += 1
        elif ((r_c[0]-i)**2 + (r_c[1]-j)**2)**0.5 <= h/2:
            result += 1
print(result)
