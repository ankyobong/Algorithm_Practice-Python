def push_10(n, t):
    if n <= t:
        return n+10
    else:
        return n-10


def push_5(n, t):
    if n <= t:
        return n+5
    else:
        return n-5


def push_1(n, t):
    if n <= t:
        return n+1
    else:
        return n-1


n, t = map(int, input().split())
c = 0

while True:
    if n == t:
        break

    if abs(t-n) >= 10:
        n = push_10(n, t)
        c += 1
        continue

    elif abs(t-n) >= 5:
        n1 = push_10(n, t)
        n2 = push_5(n, t)
        if abs(t-n1) < abs(t-n2):
            n = n1
        else:
            n = n2
        c += 1
        continue

    else:
        n1 = push_5(n, t)
        n2 = push_1(n, t)
        if abs(t-n1) < abs(t-n2):
            c += abs(t-n1)+1
        else:
            c += abs(t-n2)+1
        break

print(c)
