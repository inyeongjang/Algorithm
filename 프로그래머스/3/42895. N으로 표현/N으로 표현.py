def solution(N, number):
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        for k in range(1, i):
            for a in dp[i - k]:
                for b in dp[k]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)

        if number in dp[i]:
            return i

    return -1