# https://www.acmicpc.net/problem/4949
import sys

while True:
    n = sys.stdin.readline()
    if n == '.':
        print('yes')
        break
    result = list()
    for i in n:
        if i in ('[', '('):
            result.append([i])
        elif i in (']', ')'):
            if result[-1] == i:
                result.pop()
            elif i == ']' and result[-1] == '(':
                break
            elif i == ')' and result[-1] == '[':
                break
    if result:
        print('no')
    else:
        print('yes')
