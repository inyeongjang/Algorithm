# 시간 복잡도 : O(n), 공간 복잡도 : O(n)
# 각 숫자는 answer에 한 번 들어가고, 최대 한 번 pop 된다. 

def solution(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1

        answer.append(num)

    if k > 0:
        answer = answer[:-k]

    return ''.join(answer)