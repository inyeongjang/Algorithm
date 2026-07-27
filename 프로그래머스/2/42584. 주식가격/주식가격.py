def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for current in range(n):
        while stack and prices[stack[-1]] > prices[current]:
            previous = stack.pop()
            answer[previous] = current - previous

        stack.append(current)

    while stack:
        previous = stack.pop()
        answer[previous] = n - 1 - previous

    return answer