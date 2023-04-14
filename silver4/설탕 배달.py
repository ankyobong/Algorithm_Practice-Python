# https://www.acmicpc.net/problem/2839
# n = int(input())
# m = n//5
# result = -1
#
# for i in reversed(range(1, m+1)):
#     if (n-(i*5)) % 3 == 0:
#         result = i + ((n-(i*5))//3)
#         break
#
# if result == -1 and n % 3 == 0:
#     result = n//3
#
# print(result)


x = int(input())
a = 0
while x >= 0:
    if x % 5 == 0:
        a += (x//5)
        print(a)
        break
    x = x - 3
    a = a + 1
else:
    print(-1)
