f_list = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    f_list[a] = b
    
s_list = list(f_list.keys())
s_list.sort()

for i in s_list:
    print(i, f_list[i])
