def solution(number, hand):
    a = []
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left = '*'
    right = '#'

    for i in number:
        N_row, L_row, R_row = 0, 0, 0
        N_col, L_col, R_col = 0, 0, 0
        for j in range(len(b)):
            try:
                if i in b[j]:
                    N_row = j
                    N_col = b[j].index(i)
                if left in b[j]:
                    L_row = j
                    L_col = b[j].index(left)
                if right in b[j]:
                    R_row = j
                    R_col = b[j].index(right)
            except:
                pass
        if i in [1, 4, 7, '*']:
            a.append('L')
            left = i
        elif i in [3, 6, 9, '#']:
            a.append('R')
            right = i
        else:
            d_l = abs(N_row-L_row)+abs(N_col-L_col)
            d_r = abs(N_row-R_row)+abs(N_col-R_col)
            if d_r == d_l:
                if hand =='right':
                    a.append('R')
                    right = i
                else:
                    a.append('L')
                    left = i
            elif d_l > d_r:
                a.append('R')
                right = i
            else:
                a.append('L')
                left = i

    return "".join(a)


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
