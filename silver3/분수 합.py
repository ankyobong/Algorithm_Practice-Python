# https://www.acmicpc.net/problem/1735
import fractions
a, b = map(int, input().split())
c, d = map(int, input().split())

x, y = 0, 0
if b == d:
    x = a + c
    y = b
else:
    x = (a*d) + (c*b)
    y = b * d

Irr = fractions.Fraction(x, y)

print(Irr.numerator, Irr.denominator)
