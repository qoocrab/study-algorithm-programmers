# 시간복잡도 - O(n), 공간복잡도 - O(1)
def solution(array, height):
    return sum([1 if n > height else 0 for n in array])
