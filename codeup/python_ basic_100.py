# 01 기초 출력
print("Hello")

# 02
print("Hello World")

# 03
print("Hello")
print("World")

# 04
print("'Hello'")

# 05
print('"Hello World"')

# 06
print('''"!@#$%^&*()'
      ''')
# 07
print('''"C:\Download\\'hello'.py"
      ''')
# 08
print("""print("Hello\\nWorld")
      """)
# 09
c = input()
print(c)

# 10
c = int(input())
print(c)

# 11
c = float(input())
print(c)

# 12
a, b = int(input()), int(input())
print('%s\n%s' % (a, b))

# 13
a, b = input(), input()
print('%s\n%s' % (b, a))

# 14
f = float(input())
print('%s\n%s\n%s' % (f, f, f))

# 15
a, b = input().split()
print('%s\n%s' % (a, b))

# 16
a, b = input().split()
print('%s %s' % (b, a))

# 17
a = input()
print(a, a, a)

# 18
a, b = input().split(':')
print(a, b, sep=':')

# 19
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 20
a, b = input().split('-')
print(a+b)

# 21
s = input()
for i in range(len(s)):
    print(s[i])

# 22
s = input()
print(s[0:2], s[2:4], s[4:6])

# 23
s = input().split(':')
print(s[1])

# 24
w1, w2 = input().split()
print(w1 + w2)

# 25
a, b = input().split()
print(int(a) + int(b))

# 26
a = input()
b = input()
print(float(a)+float(b))

# 27
a = int(input())
print('%x' % a)

# 28
a = int(input())
print('%X' % a)

# 29
a = int(input(), 16)
print('%o' % a)

# 30
a = ord(input())
print(a)

# 31
c = int(input())
print(chr(c))

# 32
c = int(input())
print(-c)

# 33
a = ord(input())
print(chr(a+1))

# 34
a, b = input().split()
print(int(a) - int(b))

# 35
a, b = input().split()
print(float(a) * float(b))

# 36
w, n = input().split()
print(w*int(n))

# 37
n = input()
s = input()
print(int(n)*s)

# 38
a, b = input().split()
print(int(a)**int(b))

# 39
a, b = input().split()
print(float(a)**float(b))

# 40
a, b = input().split()
print(int(a)//int(b))

# 41
a, b = input().split()
print(int(a)%int(b))

# 42
a = float(input())
print(format(a, ".2f"))

# 43
a, b = input().split()
print(format(float(a)/float(b), ".3f"))

# 44
a, b = input().split()
print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(a) // int(b))
print(int(a) % int(b))
print(format(int(a) / int(b), '.2f'))

# 45
a, b, c = input().split()
d = int(a) + int(b) + int(c)
print(d, format(d/3, '.2f'))

# 46
a = input()
print(int(a) << 1)

# 47
a, b = input().split()
print(int(a) << int(b))

# 48
a, b = input().split()
print("True") if int(a) < int(b) else print("False")

# 49
a, b = input().split()
print("True") if int(a) == int(b) else print("False")

# 50
a, b = input().split()
print("True") if int(a) <= int(b) else print("False")

# 51
a, b = input().split()
print("True") if int(a) != int(b) else print("False")

# 52
n = int(input())
print(bool(n))

# 53
a = bool(int(input()))
print(not a)

# 54
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 55
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 56
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))

# 57
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or ((not a) and (not b)))

# 58
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not(a or b))

# 59 비트연산자
a = int(input())
print(~a)

# 60
a, b = input().split()
print(int(a) & int(b))

# 61
a, b = input().split()
print(int(a) | int(b))

# 62
a, b = input().split()
print(int(a) ^ int(b))

# 63
a, b = input().split()
a = int(a)
b = int(b)
print(a if (a >= b) else b)

# 64
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a if a < b else b) if ((a if a < b else b) < c) else c)

# 65
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a % 2 == 0:
    print(a)

if b % 2 == 0:
    print(b)

if c % 2 == 0:
    print(c)

# 66
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a % 2 == 0:
    print('even')
else:
    print('odd')
if b % 2 == 0:
    print('even')
else:
    print('odd')
if c % 2 == 0:
    print('even')
else:
    print('odd')

# 67
n = int(input())
if n < 0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')

# 68
n = int(input())
if n >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')

# 69
a = input()
if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else:
    print('what?')

# 70
a = int(input())
if a//3 == 1:
    print("spring")
elif a//3 == 2:
    print("summer")
elif a//3 == 3:
    print("fall")
else:
    print("winter")

# 71
n = 1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)

# 72
n = int(input())
while n != 0:
    print(n)
    n -= 1

# 73
n = int(input())
while n != 0:
    n -= 1
    print(n)

# 74
c = ord(input())
t = ord('a')
while t <= c:
    print(chr(t), end=' ')
    t += 1

# 75
c = int(input())
t = 0
while t <= c:
    print(t)
    t += 1

# 76
n = int(input())
for i in range(n + 1):
    print(i)

# 77
n = int(input())
s = 0
for i in range(1, n+1):
    if i % 2 == 0:
        s += i
print(s)

# 78
s = None
while s != 'q':
    s = input()
    print(s)

# 79
n = int(input())
i, s = 0, 0
while s < n:
    i += 1
    s += i
print(i)

# 80
n, m = input().split()
for i in range(1, int(n)+1):
    for j in range(1, int(m)+1):
        print(i, j)

# 81
s = int(input(), 16)
if 9 < s < 17:
    for i in range(1, 16):
        print('%X*%X=%X' % (s, i, s*i))

# 82
s = int(input())
if s < 30:
    for i in range(1, s+1):
        i = str(i)
        if i.count('3') == 1 or i.count('6') == 1 or i.count('9') == 1:
            print('X', end=' ')
        else:
            print(i, end=' ')

# 83
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
c = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            c += 1
print(c)

# 84
h, b, c, s = input().split()
bit = int(h) * int(b) * int(c) * int(s) / 8 / 1024 / 1024
print(format(bit, '.1f'), 'MB')

# 85
w, h, b= input().split()
bit = int(w) * int(h) * int(b) / 8 / 1024 / 1024
print(format(bit, '.2f'), 'MB')

# 86
n = int(input())
a, b = 0, 0
while b < n:
    a += 1
    b += a
print(b)

# 87
n = int(input())
for i in range(1, n+1):
    if i % 3 != 0:
        print(i, end=' ')

# 88
a, d, n = input().split()
a = int(a)
for i in range(1, int(n)):
    a += int(d)
print(a)

# 89
a, d, n = input().split()
a = int(a)
for i in range(1, int(n)):
    a *= int(d)
print(a)

# 90
a, m, d, n = input().split()
a = int(a)
d = int(d)
m = int(m)
for i in range(1, int(n)):
    a = a * m + d
print(a)

# 91
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)

# 92
n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
d = [0 for i in range(23)]
for i in a:
    d[i-1] += 1
for i in d:
    print(i, end=' ')

# 93
n = int(input())
a = input().split()
for i in range(n-1, -1, -1):
    print(a[i], end=' ')

# 94
n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(min(a))

# 95
d = [[0 for j in range(20)] for i in range(20)]
n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

# 96
d = [0 for i in range(19)]
for i in range(19):
    d[i] = (list(map(int, input().split())))
n = int(input())
for i in range(n):
    x, y = input().split()
    for j in range(19):
        if d[j][int(y)-1] == 0:
            d[j][int(y)-1] = 1
        else:
            d[j][int(y)-1] = 0

        if d[int(x)-1][j] == 0:
            d[int(x)-1][j] = 1
        else:
            d[int(x)-1][j] = 0
for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()

# 97
h, w = map(int, input().split())
a = [[0 for j in range(w)] for i in range(h)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            a[x-1][y-1+j] = 1
        else:
            a[x-1+j][y-1] = 1
for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()

# 98
a = [[0 for z in range(10)] for y in range(10)]
for i in range(10):
    a[i] = list(map(int, input().split()))
c, d = 1, 1
for i in range(1,10):
    for j in range(1,10):
        if a[i][j] == 0 and c == j:
            a[i][j] = 9
            c = j+1
        elif a[i][j] == 1 and d == i and c == j:
            c = j-1
            d = i+1
        elif a[i][j] == 2 and d == i and c == j:
            a[i][j] = 9
            c = None
            d = None
for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()