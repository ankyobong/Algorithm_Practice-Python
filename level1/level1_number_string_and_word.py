def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i,word in enumerate(words):
        s = s.replace(word, str(i))

    return int(s)

print(solution("one4seveneight"))