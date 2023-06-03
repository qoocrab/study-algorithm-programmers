import heapq


# 시간복잡도 - O(n), 공간복잡도 - O(1)
def solution(numbers):
    heap = []

    for num in numbers:
        heapq.heappush(heap, num)
        if len(heap) > 2:
            heapq.heappop(heap)

    return heapq.heappop(heap) * heapq.heappop(heap)
