# https://www.acmicpc.net/problem/1925
x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
z1, z2 = map(int, input().split())

xy = abs(x1-y1)**2 + abs(x2-y2)**2
yz = abs(z1-y1)**2 + abs(z2-y2)**2
xz = abs(z1-x1)**2 + abs(z2-x2)**2

l1 = [xy, yz, xz]
l2 = [xy**0.5, yz**0.5, xz**0.5]
l1.sort()
l2.sort()

if l2[2] >= l2[0]+l2[1]:
    print('X')
elif l1[0] == l1[1] and l1[1] == l1[2]:
    print('JungTriangle')
elif l1[0] == l1[1]:
    if (l1[0]+l1[1])**0.5 == l2[2]:
        print('Jikkak2Triangle')
    else:
        print('Dunkak2Triangle')
elif l1[2] == l1[1]:
    print('Yeahkak2Triangle')
else:
    if (l1[0]+l1[1])**0.5 == l2[2]:
        print('JikkakTriangle')
    elif (l1[0]+l1[1])**0.5 < l2[2]:
        print('DunkakTriangle')
    else:
        print('YeahkakTriangle')
