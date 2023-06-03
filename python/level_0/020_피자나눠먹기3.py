import math


# 시간복잡도 - O(1), 공간복잡도 - O(1)
def solution(slice, n):
    return math.ceil(n / slice)
