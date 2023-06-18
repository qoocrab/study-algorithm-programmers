# 시간복잡도 - O(n), 공간복잡도 - O(1)
def solution(my_string):
    return my_string.translate(str.maketrans("", "", "aeiou"))
