import datetime
a = int(input())
data = list()

for _ in range(a):
    name = list(input().split())
    dt = datetime.date(year=int(name[1]), month=int(name[2]), day=int(name[3]))
    data.append([name[0], dt])

data = sorted(data, key=lambda a: a[0])
s = sorted(data, key=lambda a: a[1])


for i, _ in enumerate(s):
    print(s[i][0])
