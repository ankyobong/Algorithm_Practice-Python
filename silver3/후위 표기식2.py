# https://www.acmicpc.net/problem/1935
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
q = input()
numbers = []
for i in range(n):
    numbers.append(int(input()))
result = []

for i in q:
    if i.isalpha():
        result.append(numbers[alp.index(i)])
    else:
        b = result.pop()
        a = result.pop()
        if i == '+':
            result.append(a+b)
        elif i == '-':
            result.append(a-b)
        elif i == '*':
            result.append(a*b)
        elif i == '/':
            result.append(a/b)

print('{:.2f}'.format(round(result[0], 2)))
