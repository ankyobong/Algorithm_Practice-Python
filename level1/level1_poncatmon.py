def solution(nums):
    n = int(len(nums)/2)
    answer = len(set(nums))
    if answer > n:
        answer = n

    return answer


def best_solution(nums):
    return min(len(nums)/2, len(set(nums)))


print(solution([3, 3, 3, 2, 2, 2]))
