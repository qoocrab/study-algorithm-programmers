# 시간복잡도 - O(d), 공간복잡도 - O(d), d = 입력 정수의 자릿수
def solution(n):
    return sum(int(num) for num in str(n))
