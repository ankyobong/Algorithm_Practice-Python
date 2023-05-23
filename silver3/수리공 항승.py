# https://www.acmicpc.net/problem/1449
n, l = map(int, input().split())
fix_l = list(map(int, input().split()))
fix_l.sort()
start = fix_l[0]
count = 1

for point in fix_l:
    if point in range(start, start+l):
        continue
    else:
        start = point
        count += 1

print(count)
