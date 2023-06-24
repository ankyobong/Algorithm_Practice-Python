# https://www.acmicpc.net/problem/1181
# a = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
import sys


a = set()
for i in range(int(input())):
    a.add(sys.stdin.readline().rstrip())
a = list(a)
a.sort()
a.sort(key=lambda x: len(x))
print('\n'.join(a))
# s_list = sorted(a, key=lambda a: len(a), reverse=False)
# print('\n'.join(s_list))

# sorted 보다 리스트에 내장함수 적용하는게 더 좋음.
# 값입력시 함수 사용하면 더빠르게 읽음.

