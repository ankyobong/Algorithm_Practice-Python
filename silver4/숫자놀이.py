# https://www.acmicpc.net/problem/1755
m, n = map(int, input().split())
a_d = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
       "8": "eight", "9": "nine"}
result = {}
for i in range(m, n+1):
    word = ""
    for j in str(i):
        word += a_d[j] + " "
    result[word[:-1]] = i
count = 1
for i in sorted(result):
    if count == 10:
        count = 1
        print(result[i])
    else:
        count += 1
        print(result[i], end=' ')
