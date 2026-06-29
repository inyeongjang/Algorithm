def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    giver = []
    receiver = [] 
    
    for i in lost:
        for j in reserve:
            if (i == j):
                receiver.append(i)
                giver.append(i)
                break 
        
    for i in lost:
        if i not in receiver:
            for j in reserve:
                if j not in giver:
                    if (i - 1 == j):
                        receiver.append(i)
                        giver.append(j)
                        break 
                    if (i + 1 == j):
                        receiver.append(i)
                        giver.append(j)
                        break 
                        
    answer = n - len(lost) + len(receiver)
    
    return answer