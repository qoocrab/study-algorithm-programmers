# 시간복잡도 - O(1), 공간복잡도 - O(1)
def solution(sides):
    a, b, c = sorted(sides)

    return 1 if c < a + b else 2
