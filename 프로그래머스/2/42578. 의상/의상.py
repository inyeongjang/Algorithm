# 시간 복잡도 : O(n), 공간 복잡도 : O(n)

def solution(clothes):
    answer = 1
    clothes_count = {}
    
    for _, category in clothes:
        clothes_count[category] = clothes_count.get(category, 0) + 1 
    
    for count in clothes_count.values():
        answer *= count + 1 

    return answer - 1