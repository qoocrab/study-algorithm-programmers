# 시간복잡도 - O(m), 공간복잡도 - O(1), m은 control의 길이
def solution(n, control):
    operations = {"w": 1, "s": -1, "d": 10, "a": -10}

    for c in control:
        n += operations[c]

    return n
