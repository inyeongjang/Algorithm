# 시간 복잡도 : O(n²), 공간 복잡도 : O(n)

from collections import deque 

def solution(begin, target, words):
    
    def can_change(a, b):
        count = 0
        
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        
        return count == 1
    
    queue = deque()
    queue.append((begin, 0))
    
    visited = [False] * len(words)
    
    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            return steps
        
        for i in range(len(words)):
            if not visited[i] and can_change(current, words[i]):
                    visited[i] = True 
                    queue.append((words[i], steps + 1))   
    
    return 0