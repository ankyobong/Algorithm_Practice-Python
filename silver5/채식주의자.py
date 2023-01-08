# https://www.acmicpc.net/problem/2936
x, y = map(int, input().split())
s = 31250  # 한변의 넓이
l = 125  # 빗변의 제곱
r_x, r_y = 0, 0
if x == 0:
    if y == 0:
        r_x = r_y = l
    elif y < l:
        r_x = s/(250 - y)
        r_y = 250 - r_x
    else:
        r_x = s/y
elif y == 0:
    if x < l:
        r_y = s/(250-x)
        r_x = 250 - r_y
    else:
        r_y = s/x
else:
    if x < l:
        r_x = 250-s/y
    else:
        r_y = 250-s/x
print("%.2f %.2f" % (r_x, r_y))
