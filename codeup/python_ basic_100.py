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
