# https://www.acmicpc.net/problem/1978

n = int(input())
numbers = map(int, input().split())
count = 0
for num in numbers:
    is_sosu = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_sosu = False
                break
        if is_sosu:
            count += 1

print(count)
