def solution(prices):
    answer = []

    for i in range(len(prices)):
        sec = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                sec += 1
            else:
                sec += 1
                break 
        answer.append(sec)
    
    return answer

"""
1. 모든 요소에 대해 순회
2. sec <- 0
3. 현재 가격의 다음 요소부터 순회 
4. if 현재 가격 <= 다음 가격 : sec++
   else : break 
   answer 배열에 sec 삽입
"""