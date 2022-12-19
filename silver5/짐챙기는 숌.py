# https://www.acmicpc.net/problem/1817

# n,m,*l=map(int,open(0).read().split()) 인풋받는법 괜찮은데..?
n, m = map(int, input().split())
if n != 0:
    box = input().split()
    temp = 0
    box_n = 1
    for i in box:
        if m >= int(i)+temp:
            temp += int(i)
        else:
            box_n += 1
            temp = int(i)
    print(box_n)
else:
    print(0)
