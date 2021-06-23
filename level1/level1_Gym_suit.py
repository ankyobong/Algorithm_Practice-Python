def solution(n, lost, reserve):
    temp = [1 for i in range(n)]
    answer = 0
    lost = list(set(lost))
    reserve = list(set(reserve))
    for i in lost:
        i -= 1
        temp[i] -= 1
    for i in reserve:
        i -= 1
        temp[i] += 1

    for i in range(len(temp)):
        if temp[i] == 2:
            if i-1 != -1 and temp[i-1] == 0:
                temp[i] -= 1
                temp[i-1] += 1
            elif i+1 != n and temp[i+1] == 0:
                temp[i] -= 1
                temp[i+1] += 1

    for i in range(n):
        if temp[i] > 0:
            answer += 1
    return answer


def best_solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


a = best_solution(5, [2, 4], [1, 2, 3, 5])
print(a)
