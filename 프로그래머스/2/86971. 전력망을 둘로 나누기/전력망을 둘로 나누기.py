# 시간 복잡도: O(n²), 공간 복잡도: O(n)

def solution(n, wires):
    answer = n

    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)

        for j in range(len(wires)):
            if i == j:
                continue

            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            visited[node] = True

            for next_node in graph[node]:
                if not visited[next_node]:
                    dfs(next_node)

        dfs(1)

        count = sum(visited)
        answer = min(answer, abs(count - (n - count)))

    return answer