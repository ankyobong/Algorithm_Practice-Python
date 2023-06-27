a = int(input())
data = list(map(int, input().split()))


def rank(data, k):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == k:
            return mid
        elif data[mid] < k:
            start = mid + 1
        else:
            end = mid - 1


def resort(data):
    output = ""
    s_data = sorted(data)
    for k in data:
        output += str(rank(s_data, k)) + ' '
    return output


print(resort(data))
