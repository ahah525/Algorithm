from collections import deque

# BFS 메서드
def bfs(graph, start, visited):
  # 큐 구현을 위한 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드 방문 처리
  visited[start] = True

  # 큐가 빌 때가지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')

    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
  
  
# 각 노드가 연결된 정보(2차원 리스트)
graph = [
  [],   # 노드 번호가 1번부터 시작하므로 비워두는게 좋음
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9  # 노드 개수보다 1개 크게 생성

bfs(graph, 1, visited)