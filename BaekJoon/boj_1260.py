from collections import deque

# 정점 개수, 간선 개수, 탐색 시작 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

# 그래프 정보
for i in range(m):
  # 연결된 두 정점
  a, b = map(int, input().split()) 
  graph[a].append(b)
  graph[b].append(a)
# 각 정점별 인접 노드 번호 오름 차순 정렬
for i in graph:
  i.sort()    

# DFS
def dfs(v):
  # 현재 노드 삽입, 방문처리
  visited[v] = True
  print(v, end=" ")

  # 인접 노드 탐색
  for i in graph[v]:
    # 방문하지 않은 노드이면
    if not visited[i]:
      dfs(i)
  
# BFS
def bfs(v):
  queue = deque()
  # 시작점 삽입, 방문처리
  queue.append(v)
  visited[v] = True

  while queue:
    # 꺼내기
    v = queue.popleft()
    print(v, end=" ")
    
    # 꺼낸 노드의 인접 노드 탐색
    for i in graph[v]:
      # 가보지 않은 곳이면
      if not visited[i]:
        # 삽입, 방문처리
        queue.append(i)
        visited[i] = True

dfs(v)
print()
visited = [False] * (n + 1)  # 방문 여부 초기화
bfs(v)