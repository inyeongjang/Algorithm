"""
    시간 복잡도 : O(√N), 공간 복잡도 : O(1)
    
    w * h = brown + yellow 
    yellow = (h - 2) * (w - 2)
    brown = 2 * w + 2 * h - 4
"""

def solution(brown, yellow):
    total = brown + yellow 
    
    for h in range(1, int(total ** 0.5) + 1) :
        if total % h == 0:
            w = total // h 
            
            if brown == 2 * (w + h) - 4:
                return [w, h]