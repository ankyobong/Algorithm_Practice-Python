# https://www.acmicpc.net/problem/1920
import sys

sys.stdin.readline()
# set으로 받으면 탐색시간이 줄어듦
a = set(sys.stdin.readline().split())
sys.stdin.readline()
b = [*sys.stdin.readline().split()]
for i in b:
    if i in a:
        print(1)
    else:
        print(0)
