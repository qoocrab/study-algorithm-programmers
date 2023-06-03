# 시간복잡도 - O(n), 공간복잡도 - O(1)
def solution(num_list):
    return [
        sum(1 for num in num_list if num % 2 == 0),
        sum(1 for num in num_list if num % 2 != 0),
    ]
