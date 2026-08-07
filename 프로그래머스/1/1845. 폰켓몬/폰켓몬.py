# 시간 복잡도 : O(n), 공간 복잡도 : O(n)

def solution(nums):
    return min(len(nums) // 2, len(set(nums)))