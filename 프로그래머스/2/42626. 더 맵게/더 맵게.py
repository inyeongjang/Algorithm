# heapq : 최소 힙 자료구조
# 시간 복잡도 : O(n log n), 공간 복잡도 : O(1)

import heapq 

def solution(scoville, K):
    answer = 0
    
    # heapify : 리스트를 최소 힙으로 변환 -> O(n)
    heapq.heapify(scoville)

    # 최대 n번 반복
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        # heappop : 최솟값 제거 -> O(log n)
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # heappush : 삽입 -> O(log n)
        heapq.heappush(scoville, first + 2 * second)
        answer += 1

    return answer