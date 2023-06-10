# https://www.acmicpc.net/problem/1544
n = int(input())
words = list()
for _ in range(n):
    words.append(input())
    
result = 0
# 중복제거
words = list(set(words))
while len(words) != 0:
    word = words[0]
    for i in range(len(word)):
        if word in words:
            words.remove(word)
        if len(word) > 1:
            word = word[1:] + word[0]
    result += 1

print(result)
