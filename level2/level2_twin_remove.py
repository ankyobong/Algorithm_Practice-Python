def solution(s):
    a = [0]
    s = ",".join(s)
    s = s.split(',')
    for j in s:
        if a[-1] == j:
            a.pop(-1)
        else:
            a.append(j)
    if len(a) == 1:
        return 1
    else:
        return 0


print(solution('baabaa'))
print(solution('cdcd'))
