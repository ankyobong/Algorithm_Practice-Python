# https://www.acmicpc.net/problem/1436
# 1666,2666,3666,4666,5666,6660,6661,6662,6663,6664,6665,6666,6667,6668,6669,7666

num = int(input())
count = 0
start = 666
while True:
    if '666' not in str(start):
        start += 1
        continue
    count += 1
    if count == num:
        print(start)
        break
    start += 1
