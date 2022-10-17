# https://www.acmicpc.net/problem/1380

wave = 1
while True:
    scenario = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        scenario.append([input()])
    for i in range(n*2-1):
        temp = input()
        num = temp.split()
        if len(num) == 1:
            n = int(num[0])
            break
        scenario[int(num[0])-1].append(num[1])
    for j in scenario:
        if len(j) == 2:
            print(wave, j[0])
    wave += 1

    # wave = 1
    # while True:
    #     scenario = {}
    #     n = int(input())
    #     if n == 0:
    #         exit()
    #     for i in range(n):
    #         scenario[str(i + 1)] = input().strip()
    #     for j in range(n * 2 - 1):
    #         num, status = input().split()
    #         if j >= n:
    #             del scenario[num]
    #
    #     print(wave, list(scenario.values())[0])
    #     wave += 1