# https://www.acmicpc.net/problem/1384
group = 1
while True:
    members = int(input())
    if members == 0:
        break
    print(f'Group {group}')
    team = []
    check = True
    for _ in range(members):
        team.append(input().split())
    for nt, i in enumerate(team, 1):
        for n, j in enumerate(i, 1):
            if j == 'N':
                check = False
                print(f'{team[nt - n][0]} was nasty about {i[0]}')
    if check:
        print('Nobody was nasty')
    print('')
    group += 1
