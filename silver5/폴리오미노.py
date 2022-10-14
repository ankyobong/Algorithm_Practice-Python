# https://www.acmicpc.net/problem/1343
board=input().replace('XXXX','AAAA').replace('XX','BB')
if 'X' in board:
    print(-1)
else:
    print(board)