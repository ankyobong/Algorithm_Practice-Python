# https://www.acmicpc.net/problem/1639
num = list(map(int, list(input())))
result = 0

for i in range(len(num)):
    for j in range(i+1, len(num), 2):
        t = num[i:j+1]
        if sum(t[:len(t)//2]) == sum(t[len(t)//2:]):
            if result < len(t):
                result = len(t)

print(result)
