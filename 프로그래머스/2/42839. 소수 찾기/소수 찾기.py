import itertools

def solution(numbers):
    answer = 0
    numbers_arr = []
    numbers_set = set()
    
    for i in range(len(numbers)):
        numbers_arr.append(itertools.permutations(numbers, i + 1))
    
    for permutations in numbers_arr:
        for p in permutations:
            numbers_set.add(int("".join(p)))
    
    for number in numbers_set:
        answer += 1 
        if number < 2:
            answer -= 1
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                answer -= 1
                break 
                
    return answer