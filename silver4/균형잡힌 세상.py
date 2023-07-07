# https://www.acmicpc.net/problem/4949
import sys, re

a = ''
while True:
    a += sys.stdin.readline().rstrip()
    if a == '.':
        break
    elif a[-1] != '.':
        continue
        
    n = re.sub(r'([a-z,A-Z," "])', '', a)
    result = list()
    for i in n:
        if i in ('[', '('):
            result.append(i)
        elif i in (']', ')'):
            if result:
                if i == ']' and result[-1] == '[':
                    result.pop()
                elif i == ')' and result[-1] == '(':
                    result.pop()
                elif i == ']' and result[-1] == '(':
                    result.append(i)
                    break
                elif i == ')' and result[-1] == '[':
                    result.append(i)
                    break
            else:
                result.append(i)
                break

    if result:
        print('no')
    else:
        print('yes')
    a = ''
