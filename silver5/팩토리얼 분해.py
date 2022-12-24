# https://www.acmicpc.net/problem/2057
import math
n = int(input())
result = 0
fac_num = [math.factorial(i) for i in range(21)]

if n == 0:
    print('NO')
else:
    for i in range(20, -1,-1):
        if n >= fac_num[i]:
            n -= fac_num[i]

    print("YES") if n == 0 else print('NO')