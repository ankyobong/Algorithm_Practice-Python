# https://www.acmicpc.net/problem/2161
n = [i+1 for i in range(1, int(input()))]
result = '1'
while n:
    n.append(n.pop(0))
    if n:
        result += f' {n.pop(0)}'
print(result)
