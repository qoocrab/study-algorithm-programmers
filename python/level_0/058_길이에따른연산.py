from math import prod


# 시간복잡도 - O(n), 공간복잡도 - O(1)
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return prod(num_list)
