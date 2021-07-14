n = int(input())
change = 0
for money in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
    change += n // money
    n = n % money
print(change)