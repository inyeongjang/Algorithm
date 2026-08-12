# 시간 복잡도 : O(n! * √M), 공간 복잡도 : O(n!)

import itertools

def solution(numbers):
    answer = 0
    numbers_set = set()
    
    for i in range(1, len(numbers) + 1):
        for p in itertools.permutations(numbers, i):
            numbers_set.add(int("".join(p)))
    
    for number in numbers_set:
        if number < 2:
            continue 
        
        is_prime = True 
        
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False  
                break 
        
        if is_prime:
            answer += 1 
            
    return answer