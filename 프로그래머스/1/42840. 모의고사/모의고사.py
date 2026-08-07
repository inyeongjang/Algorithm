def solution(answers):
    answer = []
    score = {1 : 0, 2 : 0, 3 : 0}
    
    answer_1 = list(i % 5 + 1 for i in range(len(answers)))

    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_2 = list(pattern_2[i % len(pattern_2)] for i in range(len(answers)))
    
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]       
    answer_3 = list(pattern_3[i % len(pattern_3)] for i in range(len(answers)))
    
            
    for i in range(len(answers)):
        if answers[i] == answer_1[i]:
            score[1] += 1 
        if answers[i] == answer_2[i]:
            score[2] += 1
        if answers[i] == answer_3[i]:
            score[3] += 1
    
    score = list(score.items())
    score.sort(key=lambda x: x[1], reverse=True)
    
    answer.append(score[0][0])
    
    if score[0][1] == score[1][1]:
        answer.append(score[1][0])
        if score[0][1] == score[2][1]:
            answer.append(score[2][0])
        
    answer.sort() 
    
    return answer