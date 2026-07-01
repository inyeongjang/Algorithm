def solution(name):

    answer = 0
    move = len(name) - 1

    for i in range(len(name)):

        cnt = abs(ord('A') - ord(name[i]))
        answer += min(cnt, 26 - cnt)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        move = min(move, 2 * i + len(name) - next)
        move = min(move, i + 2 * (len(name) - next))
    
    return answer + move