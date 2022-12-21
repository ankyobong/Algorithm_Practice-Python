# https://www.acmicpc.net/problem/1969

num, length = map(int, input().split())
dna_list = [input() for i in range(num)]
result = ''
hp = 0
for i in range(length):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}  # 알파벳 순서
    for j in range(num):
        if dna_list[j][i] == 'A':
            count['A'] += 1
        elif dna_list[j][i] == 'C':
            count['C'] += 1
        elif dna_list[j][i] == 'G':
            count['G'] += 1
        elif dna_list[j][i] == 'T':
            count['T'] += 1
    for k, v in count.items():
        if v == max(count.values()):
            result += k
            break
    hp += sum(count.values()) - max(count.values())

print(result, hp, sep='\n')
