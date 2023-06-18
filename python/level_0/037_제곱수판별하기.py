import math


# 시간복잡도 - O(1), 공간복잡도 - O(1)
def solution(n):
    return 1 if math.isqrt(n) ** 2 == n else 2
