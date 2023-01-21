# https://www.acmicpc.net/problem/1018
n, m = map(int, input().split())
c = [input() for _ in range(n)]
n_t, m_t = n-7, m-7
result = []

for i in range(n_t):
    for j in range(m_t):
        st1, st2 = 0, 0
        for y in range(i,i+8):
            for x in range(j, j+8):
                if (x+y) % 2 ==0:
                    if c[y][x] != 'B':
                        st1 += 1
                    if c[y][x] != 'W':
                        st2 += 1
                else:
                    if c[y][x] != 'W':
                        st1 += 1
                    if c[y][x] != 'B':
                        st2 += 1
        result.append(st1)
        result.append(st2)
print(min(result))