# https://www.acmicpc.net/problem/1789
s = int(input())
i = 0
sum_i = 0
while s >= sum_i:
    i += 1
    sum_i += i
    # if s < sum_i:
    #     break
print(i-1)


# 가우스 공식
s = int(input())
r = int((s*2)**0.5)
if r * (r + 1) <= s*2:
    print(r)
else:
    print(r-1)
