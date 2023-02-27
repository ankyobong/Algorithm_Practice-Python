# https://www.acmicpc.net/problem/1622
while True:
    try:
        a = input()
        b = input()

        bd = {}
        for bb in b:
            if bb in bd:
                bd[bb] += 1
            else:
                bd[bb] = 1

        ans = ''
        for aa in a:
            if aa in b and bd[aa] > 0:
                ans += aa
                bd[aa] -= 1

        print(''.join(sorted(ans)))
    except EOFError:
        break
