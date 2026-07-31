import math 

def solution(progresses, speeds):
    
    answer = []
    days = []
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))

    count = 1
    current = days[0]
    
    for i in range(1, len(days)):
        if current < days[i]:
            answer.append(count)
            count = 1
            current = days[i]
        else:
            count += 1 
    
    answer.append(count)
                
    return answer