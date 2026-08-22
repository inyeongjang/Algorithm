def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    visited = [False] * len(tickets)
    route = ["ICN"]

    def dfs(current):
        # 모든 티켓을 사용했다면 성공
        if len(route) == len(tickets) + 1:
            return True

        for i in range(len(tickets)):
            start, end = tickets[i]

            # 현재 공항에서 출발하고, 아직 사용하지 않은 티켓이라면
            if start == current and not visited[i]:
                visited[i] = True
                route.append(end)

                # 이 경로로 모든 티켓 사용에 성공했다면 종료
                if dfs(end):
                    return True

                # 실패했다면 선택 취소
                route.pop()
                visited[i] = False

        return False

    dfs("ICN")

    return route