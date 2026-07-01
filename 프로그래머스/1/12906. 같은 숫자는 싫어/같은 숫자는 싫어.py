def solution(arr):
    
    answer = [arr[0]]
    top = 0
    
    for num in arr:
        if answer[top] != num:
            answer.append(num)
            top += 1
        
    return answer