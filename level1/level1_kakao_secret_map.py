def solution(n, arr1, arr2):

    answer, answer1 = [0 for i in range(n)], [0 for i in range(n)]
    a = [[0 for i in range(n)] for i in range(n)]
    for i, j in enumerate(arr1):
        answer[i] = list((bin(j)[2:]))
    for i, j in enumerate(arr2):
        answer1[i] = list((bin(j)[2:]))
    for i in range(n):
        for j in range(n - 1):
            if len(answer[i]) != n:
                answer[i].insert(0, '0')
    for i in range(n):
        for j in range(n-1):
            if len(answer1[i]) != n:
                answer1[i].insert(0, '0')
    for i in range(n):
        for j in range(n):
            if answer[i][j] == '1':
                a[i][j] = "#"
            elif answer1[i][j] == '1':
                a[i][j] = "#"
            else:
                a[i][j] = " "
    for i in range(n):
        a[i] = "".join(a[i])

    return a


def best_solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12=a12.rjust(n, '0')
        a12=a12.replace('1', '#')
        a12=a12.replace('0', ' ')
        answer.append(a12)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
