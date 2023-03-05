# https://www.acmicpc.net/problem/1748
n = int(input())
n_l = len(str(n))
result = 0
for i in range(n_l-1):
    result += 9 * 10 ** i * (i+1)
print(result + (n - 10**(n_l-1) + 1)*n_l)
