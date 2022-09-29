# https://www.acmicpc.net/problem/1010
testcase = int(input())
result = list()
for i in range(testcase):
    a, b = map(int, input().split())
    x, y, z = 1, 1, 1
    for j in range(1, a+1):
        x *= j
    for j in range(1, b+1):
        y *= j
    for j in range(1, b-a+1):
        z *= j
    result.append(y//(x*z))

for i in result:
    print(i)

