def solution(lottos, win_nums):
    temp, temp1, answer = [], [], []
    for i in range(6):
        if lottos[i] == 0:
            temp.append(0)
        for j in range(6):
            if lottos[i] == win_nums[j]:
                temp1.append(lottos[i])
    if not temp+temp1:
        answer.append(6)
    else:
        answer.append(7-len(temp+temp1))
    if len(temp) == 6 or not temp:
        answer.append(6)
    else:
        answer.append(7-len(temp1))
    return answer


def best_solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]    # is good

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


lottos = [1, 2, 5, 6, 7, 8]
win_nums = [20, 9, 3, 45, 4, 35]
a = solution(lottos, win_nums)
print(a)
