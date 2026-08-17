# 시간 복잡도 : O(n log n), 공간 복잡도 : O(n)

def solution(routes):
    routes.sort(key = lambda x: x[1])
    
    answer = 1
    camera = routes[0][1]
    
    for start, end in routes[1:]:
        if start > camera:
            answer += 1
            camera = end
                
    return answer