# https://www.acmicpc.net/problem/1788
n = int(input())
s = [0, 1]

if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

for i in range(2, abs(n) + 1):
    s.append((s[i - 1] + s[i - 2]) % 1000000000)

print(s[abs(n)])
