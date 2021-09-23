def solution(left, right):
    ent = 0
    for num in range(left, right+1):
        calculator = []
        for a in range(1, num+1):
            if num % a == 0:
                calculator.append(a)

        if int(len(calculator)%2) == 0:
            ent += num
        elif int(len(calculator)%2) == 1:
            ent -= num

    return ent

def bestsolution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer


print(solution(13, 17))
print(solution(1, 2))
print(bestsolution(13, 17))
print(bestsolution(1, 2))