# https://www.acmicpc.net/problem/1051
n, m = map(int, input().split())
mx = min(n, m)-1
square = []
for _ in range(n):
    square.append(input())

result = 1
while mx != 0:
    for i in range(n-mx):
        for j in range(m-mx):
            s = square[i][j]
            if s == square[i+mx][j] and s == square[i][j+mx] and s == square[i+mx][j+mx]:
                result = (mx+1)**2
                print(result)
                exit(0)
    mx -= 1


print(result)
