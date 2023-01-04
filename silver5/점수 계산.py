# https://www.acmicpc.net/problem/2822
scores = [int(input()) for _ in range(8)]
srt_s = sorted(scores)
print(sum(srt_s[3:]))
for i in range(8):
    if scores[i] in srt_s[3:]:
        print(i+1, end=' ')
