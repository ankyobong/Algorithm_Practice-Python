N, M = map(int, input().split())
data = {}
word = []

for _ in range(N):
    name, num = input().split()
    if name in data:
        data[name] += int(num)
    else:
        data[name] = int(num)

for _ in range(M):
    word.append(input())

for i in word:
    if i in data:
        print(data[i])
    else:
        print(0)
