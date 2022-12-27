# https://www.acmicpc.net/problem/2303

n = int(input())  # 사람의 수 입력
score = []        # 높은 점수 담는 리스트
for _ in range(n):
  card = list(map(int, input().split())) # 카드 입력
  max_digit = 0 # 가장 큰 일의 자리 수
  for i in range(5):
    for j in range(i + 1, 5):
      for k in range(j + 1, 5):
        digit = (card[i] + card[j] + card[k]) % 10 # 일의 자리 수 구하기
        if digit >= max_digit: # 제일 큰 수 구하기
          max_digit = digit
  score.append(max_digit)

for i in range(n - 1, -1, -1): # 두 명 이상일 경우 번호가 가장 큰 사람의 번호를 구하기 위해
  if score[i] == max(score):  # 제일 높은 점수 찾기
    print(i + 1)
    break

# n = int(input())
# a = []
# for i in range(n):
#     a.append([*map(int, input().split())])
#
# result = result_sum = [0 for i in range(len(a))]
#
# for i in range(len(a)):  # 0 1 2 3 4
#     one = 0
#     two = 1
#     three = 2
#     max_i = 0
#     count = 0
#     while count < 10:
#         sum_t = a[i][one] + a[i][two] + a[i][three]
#         if sum_t % 10 > max_i:
#             max_i = sum_t % 10
#             result[i] = max_i
#             result_sum[i] = sum_t
#         count += 1
#         if count in [1, 2]:
#             three += 1
#         elif count == 3:
#             two += 1
#             three = 3
#         elif count == 4:
#             three += 1
#         elif count == 5:
#             two += 1
#         elif count == 6:
#             one += 1
#             two = 2
#             three = 3
#         elif count == 7:
#             three += 1
#         elif count == 8:
#             two += 1
#         elif count == 9:
#             one += 1
# max_list = [i for i, value in enumerate(result) if value == max(result)]
# # max_list = list(filter(lambda x: result[x] == max(result), range(len(result))))
# max_e = -1
# for i in max_list:
#     if result_sum[i] > max_e:
#         max_e = result_sum[i]
#         winner = i
# print(winner+1)
