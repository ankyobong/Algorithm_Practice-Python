# https://www.acmicpc.net/problem/1439

line = input()
size = len(line)
count = 0
for i, j in enumerate(line):
    if i == 0:
        continue
    elif j != line[i-1]:
        count += 1
if line[0] == '1':
    if count % 2 != 0:
        table = str.maketrans('10', '01')
        line = line.translate(table)
else:
    if count % 2 == 0:
        table = str.maketrans('10', '01')
        line = line.translate(table)
count = 0
for i in range(size):
    temp = '0'*(size - i)
    while temp in line:
        line = line.replace(temp, '1' * (size - i), 1)
        count += 1

print(count)
