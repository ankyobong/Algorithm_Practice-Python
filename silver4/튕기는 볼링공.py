# https://www.acmicpc.net/problem/1876
import math


def dist(a, b, c, x, y):
    return abs(a*x + b*y + c) / ((a**2 + b**2) ** (1/2))


for _ in range(int(input())):
    t, x = map(float, input().split())
    result = "no"
    tanX = math.tan(math.radians(x))
    t *= -100.0
    d = 42.5 / tanX
    res = dist(-tanX, 1, 0, t, 0)
    while True:
        res_ = dist(-tanX, 1, 0, t, 0)
        if res_ > res:
            break
        if res_ <= 16:
            result = "yes"
            break
        t += 2.0 * d
        tanX *= -1
        res = res_
    print(result)
