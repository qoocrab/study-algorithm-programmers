# 시간복잡도 - O(1), 공간복잡도 - O(1)
def solution(n):
    even_numbers_count = n // 2
    return 2 * (even_numbers_count * (even_numbers_count + 1) / 2)
