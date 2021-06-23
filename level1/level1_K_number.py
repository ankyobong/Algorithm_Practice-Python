def solution(array, commands):
    answer = []
    for c in range(len(commands)):
        i = commands[c][0]
        j = commands[c][1]
        k = commands[c][2]
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer


def best_solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
a = solution(array, commands)
print(a)
