from itertools import permutations

def solution(k, dungeons):
    answer = []

    for p in permutations(dungeons):
        count = 0
        left = k 
        
        for dungeon in p:
            if left < dungeon[0]:
                break 
            left -= dungeon[1]
            count += 1 
        answer.append(count)
            
    return max(answer)