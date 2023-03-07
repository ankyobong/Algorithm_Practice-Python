# https://www.acmicpc.net/problem/1758
n = int(input())
people = []
result = 0

for i in range(n):
    people.append(int(input()))
for no, i in enumerate(sorted(people, reverse=True)):
    if i - no > 0:
        result += i - no
    else:
        break

print(result)
