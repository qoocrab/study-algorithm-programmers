# 시간복잡도 - O(n), 공간복잡도 - O(n)
def solution(s1, s2):
    return len(set(s1) & set(s2))
