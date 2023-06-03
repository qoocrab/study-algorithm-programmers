# 시간복잡도 - O(1), 공간복잡도 - O(1)
def solution(n, k):
    free_drinks = n // 10
    paid_drinks = k - free_drinks

    return n * 12000 + paid_drinks * 2000
