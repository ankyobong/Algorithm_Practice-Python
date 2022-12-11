a = list(map(int, input()))
a.sort(reverse=True)
for i in a:  # 출력 1등
    print(i, end='')
print(a.__str__().replace(', ', '')[1:-1])  # 2등
print(str(a).replace(', ', '')[1:-1])  # 3등

# 숏코딩
print(*sorted(input())[::-1], sep='')
