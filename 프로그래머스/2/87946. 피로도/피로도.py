# 시간 복잡도 : O(N! x N), 공간 복잡도 : O(N)

from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for p in permutations(dungeons):
        count = 0
        left = k 
        
        for dungeon in p:
            if left < dungeon[0]:
                break 
                
            left -= dungeon[1]
            count += 1 
            
        answer = max(answer, count)
            
    return answer