a = int(input())
data = list()
num_list = list()
good_data = list()

for i in range(a):
    name = list(input().split())
    if name[0] == "I":
        if name[1] not in num_list:
            data.append([name[0], int(name[1]), name[2]])
            num_list.append(name[1])
    elif name[1].isdigit():
        for n, j in enumerate(data):
            if j[1] == int(name[1]):
                del data[n]
                num_list.remove(name[1])
                break

output_list = list(map(int, input().split()))
data = sorted(data, key=lambda a:a[1])

for i in output_list:
    print(data[i-1][1], data[i-1][2])

