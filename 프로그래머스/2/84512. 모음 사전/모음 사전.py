# 시간 복잡도 : O(n), 공간 복잡도 : O(1)

def solution(word):
    answer = 0
    number = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}

    for i in range(len(word)):
        weight = sum(5 ** k for k in range(5 - i))
        answer += (number[word[i]] - 1) * weight + 1

    return answer