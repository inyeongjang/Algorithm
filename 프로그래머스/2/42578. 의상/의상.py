def solution(clothes):
    answer = 1
    
    clothes_count = {}
    
    for cloth in clothes:
        clothes_count[cloth[1]] = clothes_count.get(cloth[1], 0) + 1 
    
    for cloth in clothes_count:
        answer *= clothes_count[cloth] + 1 

    return answer - 1