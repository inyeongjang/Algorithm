# 시간 복잡도 : O(n), 공간 복잡도 : O(1)

def solution(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes) 