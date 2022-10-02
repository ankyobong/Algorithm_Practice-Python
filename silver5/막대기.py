# https://www.acmicpc.net/problem/1094

# x = int(input())
# y = [64]
# while int(sum(y)) != x:
#     y[-1] /= 2
#     if sum(y) > x:
#         continue
#     elif int(sum(y)) == x:
#         break
#     y.append(y[-1])
#
# print(len(y))
print(bin(int(input())).count('1'))
