# https://www.acmicpc.net/problem/1935
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
q = input()
nums = [int(input()) for i in range(n)]
cal = ''
result = 0

for i in q:
    if i.isalpha():
        nums[alp.index(i)]

print('{:.2f}'.format(round(result, 2)))
