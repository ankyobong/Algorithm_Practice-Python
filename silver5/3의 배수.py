# https://www.acmicpc.net/problem/1769

x = input()
num = 0
while True:
    if len(x) > 1:
        num += 1
        n = 0
        for i in x:
            n += int(i)
        x = str(n)
    else:
        if int(x) % 3 == 0:
            print(num)
            print('YES')
        else:
            print(num)
            print('NO')
        break


