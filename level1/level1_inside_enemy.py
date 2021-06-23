def solution(a, b):
    answer = []
    for i in range(len(a)):
        answer.append(a[i]*b[i])

    return sum(answer)


def best_solution(a, b):
    return sum([x*y for x, y in zip(a, b)])
