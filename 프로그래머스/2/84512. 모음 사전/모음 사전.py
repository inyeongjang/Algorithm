def solution(word):
    answer = 0 
    number = {"A" : 1, "E" : 2, "I" : 3, "O" : 4, "U" : 5}
    
    for i in range(len(word)):
        for j in range(1, number[word[i]]):
            for k in range(5 - i):
                answer += 5 ** k 
        answer += 1
            
    return answer