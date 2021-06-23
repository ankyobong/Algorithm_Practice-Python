from itertools import combinations


def is_prime_bad(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i is 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        i = list(i)
        if is_prime_bad(sum(i)):
            print("{0}를 이용해서 {1}을 만들 수 있습니다.".format(i, sum(i)))
            answer += 1
    return answer


################################################################################
def prime_number(x):
    answer = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            answer += 1
    return 1 if answer == 1 else 0


def best_solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums, 3)])


solution([1, 2, 3, 4, 6, 5])
