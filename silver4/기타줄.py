# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split())
p, s = [], []
result = 0
for _ in range(m):
    p_t, s_t = map(int, input().split())
    p.append(p_t)
    s.append(s_t)

m_p = min(p)
m_s = min(s)
if m_p < m_s * 6:
    result += (n // 6) * m_p
    if (n % 6) * m_s < m_p:
        result += (n % 6) * m_s
    else:
        result += m_p
else:
    result += m_s * n

print(result)
