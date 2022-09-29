a, b = map(int, input().split())
s_list = []

for _ in range(a):
    name, score = input().split()
    s_list.append([name, int(score)])

s_list = sorted(s_list, key=lambda a: a[1], reverse=True)

for i in range(b):
    print(s_list[i][0])

