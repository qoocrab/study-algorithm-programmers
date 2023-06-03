# 시간복잡도 - O(n), 공간복잡도 - O(1)
def solution(num_list):
    start = 0
    end = len(num_list) - 1

    while start <= end:
        num_list[start], num_list[end] = num_list[end], num_list[start]

        start += 1
        end -= 1

    return num_list
