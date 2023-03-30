# https://www.acmicpc.net/problem/1057
n, a, b = map(int, input().split())
round_v = 0

while True:
    if a == b:
        break
    a = (a+1)//2
    b = (b+1)//2
    round_v = round_v+1

print(round_v)
