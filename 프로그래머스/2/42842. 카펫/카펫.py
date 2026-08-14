def solution(brown, yellow):
    answer = []
    # w * h = brown + yellow 
    # yellow = (h - 2) * (w - 2)
    # brown = 2 * w + 2 * h - 4
    # brown + yellow 의 약수 중 조건을 만족하는 것 
    
    for i in range(1, int((brown + yellow) ** 0.5) + 1) :
        if (brown + yellow) % i == 0:
            if brown == 2 * (i + (brown + yellow) // i) - 4:
                answer.append((brown + yellow) // i)
                answer.append(i)
                
    return answer