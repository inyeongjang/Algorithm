def solution(people, limit):
    answer = 0
    top = 0 
    bottom = len(people) - 1 
    people.sort(reverse = True)
    
    while top <= bottom:
        answer += 1
        if people[top] + people[bottom] <= limit:
            bottom -= 1 
        top += 1 
    return answer 