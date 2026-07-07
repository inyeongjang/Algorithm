def solution(progresses, speeds):
    
    answer = []
    
    while progresses:
        
        count = len(progresses)
        
        for i in range(count):
            progresses[i] += speeds[i] 
        
        r_progresses = progresses[::-1]
        
        for i in range(count):
            if all(x >= 100 for x in r_progresses[i:]):
                answer.append(count - i)
                del progresses[:count - i]
                del speeds[:count - i]
                break
                
    return answer