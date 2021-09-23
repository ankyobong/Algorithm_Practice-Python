def solution(numbers):
    allnumber = [1,2,3,4,5,6,7,8,9,0]
    for number in numbers:
        allnumber.remove(number)
    return sum(allnumber)

print(solution([1,2,3,4,6,7,8,0]))