import math

a = math.factorial(int(input()))
count = 0
is_zero = False
for i in reversed(str(a)):
    if i == '0':
        count += 1
    elif count == 0:
        continue
    else:
        break
print(count)