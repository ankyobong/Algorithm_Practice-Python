# https://www.acmicpc.net/problem/1862
n = int(input())
len_n = len(str(n))
result = 0
for i in range(len_n):
    d = n % 10
    n = n//10
    if d > 4:
        result += (d-1) * (9**i)
    else:
        result += d * (9**i)
print(result)
