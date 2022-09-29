def solution(id_list, report, k):
    answer = []
    report_dic = {}
    mail = {}
    for i in id_list:
        report_dic[i] = []
        mail[i] = 0

    for i in set(report):
        re = i.split()
        report_dic[re[1]].append(re[0])

    for i in id_list:
        if len(report_dic[i]) >= k:
            for j in report_dic[i]:
                mail[j] += 1

    for i in id_list:
        answer.append(mail[i])

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2 ))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3 ))