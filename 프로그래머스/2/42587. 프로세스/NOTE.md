### 핵심 로직

1. 맨 앞 프로세스를 꺼낸다.
2. 남은 큐에 더 높은 우선순위가 있으면 맨 뒤로 보낸다.
3. 없다면 answer를 증가시킨다.
4. 실행한 위치가 location이면 answer를 반환한다.

### 복잡도

- 시간 복잡도 : O(n²)
- 공간 복잡도 : O(n)

### deque 기본 문법 

```python
from collections import deque

q = deque([1, 2, 3])

q.append(4)     # 뒤에 추가
q.appendleft(0) # 앞에 추가
q.pop()         # 뒤에서 제거
q.popleft()     # 앞에서 제거

q[0]             # 첫 요소
q[-1]            # 마지막 요소

for value in q:
  print(vaule)
```
