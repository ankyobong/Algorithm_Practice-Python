import operator


def solution(N, stages):
    answer = {}
    rank = []
    a = 0
    b = len(stages)
    for i in range(N):
        if not stages.count(i+1):
            answer[i + 1] = 0
        else:
            a = stages.count(i+1)
            answer[i+1] = float(a/b)
        b -= a
    sanswer = sorted(answer.items(), reverse=True, key=operator.itemgetter(1))
    for i in range(len(answer)):
        rank.append(sanswer[i][0])
    return rank


print(solution(5, [2, 1, 2, 2, 4, 3, 3]))
