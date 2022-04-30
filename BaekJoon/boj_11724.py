import sys
from collections import deque

# 정점 개수, 간선 개수
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = 0  # 연결 요소 개수

# 그래프 정보
for i in range(m):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

# BFS
def bfs(v):
  queue = deque()
  # 시작 노드 삽입, 방문 처리
  queue.append(v)
  visited[v] = True

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      # 방문하지 않은 노드라면
      if not visited[i]:
        # 삽입, 방문처리
        queue.append(i)
        visited[i] = True

for i in range(1, n + 1):
 # 해당 정점이 방문하지 않았다면
  if not visited[i]:
    bfs(i)
    res += 1

print(res)

'''
import sys
sys.setrecursionlimit(10**6)

# 정점 개수, 간선 개수
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = 0  # 연결 요소 개수

# 그래프 정보
for i in range(m):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

# DFS
def dfs(v):
  # 삽입, 방문 처리
  visited[v] = True

  # 인접 노드 탐색
  for i in graph[v]:
    # 방문하지 않은 노드라면
    if not visited[i]:
      dfs(i)# 재귀 호출

for i in range(1, n + 1):
 # 해당 정점이 방문하지 않았다면
  if not visited[i]:
    dfs(i)
    res += 1

print(res)
'''