# 시간복잡도 - O(1), 공간복잡도 - O(1)
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0
