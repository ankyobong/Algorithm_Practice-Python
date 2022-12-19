# https://www.acmicpc.net/problem/1769

x = input()
num = 0
while len(x) > 1:
    num += 1
    x = str(sum([int(i) for i in x]))

if x in (0, 3, 6, 9):
    print(num)
    print('YES')
else:
    print(num)
    print('NO')

