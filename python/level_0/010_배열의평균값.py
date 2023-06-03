# 시간복잡도 - O(n), 공간복잡도 - O(1)
def solution(numbers):
    total = sum(numbers)
    count = len(numbers)

    return total / count
