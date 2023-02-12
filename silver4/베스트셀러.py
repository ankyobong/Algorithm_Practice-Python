# https://www.acmicpc.net/problem/1302
# dict
books = {}
for _ in range(int(input())):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

best_v = max(books.values())
result = []
for n in books.keys():
    if books[n] == best_v:
        result.append(n)
result.sort()
print(result[0])

# list
books = []
for _ in range(int(input())):
    books.append(input())
books.sort()
print(max(books, key=books.count))
