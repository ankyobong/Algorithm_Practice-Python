e, s, m = 0, 0, 0
result = 0
a, b, c = map(int, input().split())

while True:
    if e == a and s == b and m == c:
        print(result)
        break
    else:
        e += 1
        s += 1
        m += 1
        result += 1
        if e == 16:
            e = 1
        if s == 29:
            s = 1
        if m == 20:
            m = 1
