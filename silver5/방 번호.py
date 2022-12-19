# https://www.acmicpc.net/problem/1475
import math

room_num = input()
temp = []
for no, i in enumerate(range(10)):
    temp.append(room_num.count(str(no)))

temp[6] = math.ceil((temp.pop(9)+temp[6])/2)
print(max(temp))

