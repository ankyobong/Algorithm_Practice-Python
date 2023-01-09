# https://www.acmicpc.net/problem/2941
cro_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()
result = 0
for alp in cro_a:
    if words.count(alp) > 0:
        result += words.count(alp)
        words = words.replace(alp, ' ')
words = words.replace(' ', '')
result += len(words)
print(result)
