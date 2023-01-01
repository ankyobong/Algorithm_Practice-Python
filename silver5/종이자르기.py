# https://www.acmicpc.net/problem/2628
col, row = map(int, input().split())
big_paper_r = [0 for i in range(row)]
big_paper_c = [0 for i in range(col)]
n = int(input())
c_m = 0
r_m = 0
for _ in range(n):
    cr, no = map(int, input().split())
    if cr == 1:
        for i in range(0, no):
            big_paper_c[i] += 1
            c_m += 1
    else:
        for i in range(0, no):
            big_paper_r[i] += 1
            r_m += 1
c, r = 0, 0
result = [0 for i in range(n+1)]
for i in range(c_m+1):
    if c < big_paper_c.count(i):
        c = big_paper_c.count(i)
for i in range(r_m+1):
    if r < big_paper_r.count(i):
        r = big_paper_r.count(i)
print(r*c)
