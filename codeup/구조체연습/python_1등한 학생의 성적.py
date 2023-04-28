a = int(input())
data_list = list()
no1_scores = list()
for _ in range(a):
    name = list(input().split())
    data_list.append(name)

data_list = sorted(data_list, key=lambda a: int(a[1]), reverse=True)
no1 = data_list[0]
no1_scores.append(no1[0])

for i in range(2, len(data_list[0])):
    data_list = sorted(data_list, key=lambda a: int(a[i]), reverse=True)
    for j, k in enumerate(data_list):
        if k[i] == no1[i]:
            no1_scores.append(str(j+1))
            break

print(' '.join(no1_scores))

