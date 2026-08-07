# 시간 복잡도 : O(n logn), 공간 복잡도 : O(1)

"""
def solution(participant, completion):    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]
"""

# 시간 복잡도 : O(n), 공간 복잡도 : O(n)

def solution(participant, completion):    
    count = {}
    
    for name in participant:
        count[name] = count.get(name, 0) + 1
    
    for name in completion:
        count[name] -= 1 
    
    for name in count:
        if count[name] > 0:
            return name 