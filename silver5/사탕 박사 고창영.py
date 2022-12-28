# https://www.acmicpc.net/problem/2508
test_case = int(input())
for _ in range(test_case):
    input()
    r, c = map(int, input().split())
    box = []
    for i in range(r):
        box.append(input())
    count = 0
    for y in range(r):
        for x in range(c):
            if box[y][x] == '>' and x < c-2 and box[y][x+1] == 'o' and box[y][x+2] == '<':
                count += 1
            elif box[y][x] == 'v' and y < r-2 and box[y+1][x] == 'o' and box[y+2][x] == '^':
                count += 1
    print(count)

