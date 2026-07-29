from collections import deque 

def solution(priorities, location):
    answer = 0
    
    queue = deque()
    for index, priority in enumerate(priorities):
        queue.append((priority, index))

    while queue:
        flag = 0
        current = queue.popleft()
        
        for priority, index in queue:
            if current[0] < priority:
                queue.append(current)
                flag = -1 
                break
                
        if flag == 0:
            answer += 1
            
            if current[1] == location:
                return answer 