#from collections import deque
n = int(input())  # 컴퓨터 수
m = int(input())  # 컴퓨터 간선 수
graph = [[] for _ in range(n + 1)] 
visited = [False] * (n + 1) 
res = 0  # 1이 감염시킨 컴퓨터 수

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# BFS
def bfs(v):
  queue = deque()
  # 시작 노드 삽입, 방문 처리
  queue.append(v)
  visited[v] = True

  while queue:
    global res  # 전역변수 사용    
    # 노드 꺼내기
    v = queue.popleft()
    res += 1 
    # 인접노드 탐색
    for i in graph[v]:
      # 방문하지 않은 노드라면
      if not visited[i]:
        # 삽입, 방문처리
        queue.append(i)
        visited[i] = True

# DFS
def dfs(v):
  global res  # 전역변수 사용
  # 현재 노드 삽입, 방문처리
  visited[v] = True
  res += 1
  
  # 인접 노드 검사
  for i in graph[v]:
    # 방문하지 않은 노드라면
    if not visited[i]:
      dfs(i)  # 해당 노드 재귀 호출 
      
#bfs(1)
dfs(1)
print(res - 1)


    