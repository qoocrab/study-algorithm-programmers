import math


# 시간복잡도 - O(sqrt(n)), 공간복잡도 - O(1)
def solution(n):
    count = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count
