# 시간복잡도 - O(k), 공간복잡도 - O(k), k = num2 - num1 + 1
def solution(numbers, num1, num2):
    return numbers[num1 : num2 + 1]
