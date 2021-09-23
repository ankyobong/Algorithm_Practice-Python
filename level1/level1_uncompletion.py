def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        try:
            if participant[i] != completion[i]:
                return participant[i]
        except IndexError:
            return participant[i]


# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

def best_solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(best_solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(best_solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(best_solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))