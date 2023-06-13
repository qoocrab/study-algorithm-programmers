# 시간복잡도 - O(m * n), 공간복잡도 - O(m * n), m = 문자열의 길이, n = 반복 횟수
def solution(my_string, n):
    return "".join(char * n for char in my_string)
