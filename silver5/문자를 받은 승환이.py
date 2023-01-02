# https://www.acmicpc.net/problem/2714
abc = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def decode(L, r, c):
    res = ""
    ind = 0

    for d in range(0, min(r, c), 2):
        for i in range(c - 1 - d):
            res += L[ind]
            ind += 1

        for i in range(r - 1 - d):
            res += L[ind]
            ind += c

        for i in range(c - 1 - d):
            res += L[ind]
            ind -= 1

        for i in range(r - 1 - d):
            res += L[ind]
            ind -= c

        ind += c + 1

    if r * c % 2 == 1:
        res += L[int(r * c / 2)]

    return res


def bi_to_int(x):
    r = 16
    res = 0

    for i in x:
        res += int(i) * r
        r /= 2

    return int(res)


def code_to_str(L, ln):
    res = ""
    for i in range(0, ln, 5):
        if i + 4 >= ln:
            break
        mid = L[i] + L[i + 1] + L[i + 2] + L[i + 3] + L[i + 4]
        mid = bi_to_int(mid)
        res += abc[mid]

    return res


def str_del_space(st, ln):
    tmp = 0
    for i in range(ln - 1, -1, -1):
        if st[i] != ' ':
            tmp = i
            break
    return st[0:tmp + 1]


n = int(input())

for i in range(n):
    ipt = list(input().split())
    r = int(ipt[0])
    c = int(ipt[1])
    st = ipt[2]
    length = r * c

    print(str_del_space(code_to_str(decode(st, r, c), length), int(length/5)))
