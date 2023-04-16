# https://www.acmicpc.net/problem/3036
n = int(input())

ring = [*map(int, input().split())]

for i in ring[1:]:
    t = abs(ring[0] - i)
    if t == 0 or i//t == 0:
        print(f'{ring[0]//i}/1')
    else:
        print(f'{ring[0]//t}/{i//t}')
