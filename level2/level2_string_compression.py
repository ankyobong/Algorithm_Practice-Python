def solution(s):
    mincomp = len(s)    # 압축된 최소 길이 비교 변수

    for i in range(1, len(s)//2+1):  # 1개부터 원래 문자열의 절반길이만큼
        comp = ''
        cnt = 0
        piece = s[:i]
        
        for j in range(i, len(s)+i, i):  # i부터 len(i)+i까지 i씩 더하면서
            if s[j:j+i] == piece:   # 일치하는 경우
                cnt += 1
            else:   # 일치하지 않는 경우
                if cnt:     # 만약 반복된 적이 있으면
                    comp += str(cnt+1)+piece     # 반복된만큼의 숫자 문자를 더하기
                else:
                    comp += piece
                piece = s[j:j+i]
                cnt = 0

        if len(comp) < mincomp:
            mincomp = len(comp)

    return mincomp


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))

