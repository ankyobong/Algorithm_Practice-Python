toppings = []
n_topping = int(input())
dou, topping_cost = map(int, input().split())
k_dou = int(input())

for i in range(n_topping):
    toppings.append(int(input()))
toppings.sort(reverse=True)
k_topping = 0
c_topping = 0
result = 0
a = []

for topping in toppings:
    k_topping += topping
    c_topping += topping_cost

    cal = (k_dou+k_topping)/float(dou+c_topping)
    # a.append(cal)
    if result > cal:
        break
    else:
        result = cal

print(int(result))
# print(a)
