a = int(input())

c = map(int, input().split())
data = list(c)

s_data = sorted(data, reverse=True)

for i in data:
    print(i, s_data.index(i)+1)
