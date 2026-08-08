# 시간 복잡도 : O(n logn), 공간 복잡도 : O(1O)

def solution(people, limit):
    answer = 0
    top = 0 
    bottom = len(people) - 1 
    
    # O(nlogn)
    people.sort(reverse = True)
    
    # O(n)
    while top <= bottom:
        answer += 1
        
        if people[top] + people[bottom] <= limit:
            bottom -= 1 
        
        top += 1 
    
    return answer 