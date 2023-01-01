# https://www.acmicpc.net/problem/2581
m = int(input())
n = int(input())
count = []
for num in range(m, n + 1):
    is_sosu = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_sosu = False
                break
        if is_sosu:
            count.append(num)
if count:
    print(sum(count), count[0], sep='\n')
else:
    print(-1)
