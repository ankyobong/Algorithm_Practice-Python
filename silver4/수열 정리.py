# https://www.acmicpc.net/problem/1015
n = int(input())
result = []
t = [*map(int, input().split())]
s_t = sorted(t)
for i in range(n):
    no = s_t.index(t[i])
    result.append(no)
    s_t[no] = 0
print(*result)
