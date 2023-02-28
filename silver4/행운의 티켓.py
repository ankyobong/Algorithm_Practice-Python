# https://www.acmicpc.net/problem/1639
num = input()
l_num = len(num)
if (lambda x: sum(x))(map(int, [*num[:int(l_num / 2)]])) == (lambda x: sum(x))(map(int, [*num[int(l_num / 2):]])):
    print(l_num)
else:
    while l_num != 0:
        for i in range(len(num)-l_num):
            if (lambda x: sum(x))(map(int, [*num[i:i+int(l_num/2)]])) == (lambda x: sum(x))(map(int, [*num[i+int(l_num/2):i+int(l_num)]])):
                print(l_num)
                exit(0)
        l_num -= 1
print(0)
