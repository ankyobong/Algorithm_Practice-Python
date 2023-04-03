# https://www.acmicpc.net/problem/1985
import sys

def check_friend(x, y):
    return set(x) == set(y)


def check_almost_friend(x, y):
    for i in range(len(y) - 1):
        a, b = str(int(y[i]) + 1), str(int(y[i + 1]) - 1)
        if len(a) == 1 and len(b) == 1:
            if check_friend(x, y[:i] + y[i+2:] + a + b):
                return True
        a, b = str(int(y[i]) - 1), str(int(y[i + 1]) + 1)
        if len(a) == 1 and len(b) == 1:
            if check_friend(x, y[:i] + y[i+2:] + a + b):
                if i > 0 or a != '0':
                    return True
    return False


for _ in range(3):
    x, y = map(set, sys.stdin.readline().split())
    if x - y == set():
        print("friends")
    elif check_almost_friend(x, y) or check_almost_friend(y, x):
        print('almost friends')
    else:
        print('nothing')


