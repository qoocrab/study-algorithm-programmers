# 시간복잡도 - O(nlogn), 공간복잡도 - O(n)
def solution(array):
    return sorted(array)[(len(array) - 1) // 2]
