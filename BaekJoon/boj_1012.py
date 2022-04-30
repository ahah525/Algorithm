from collections import deque

# 위치벡터(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y):
  # 시작 좌표 삽입, 방문처리
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 좌표 범위 내이면
      if(0 <= nx < n and 0 <= ny < m):
        # 배추이면 삽입, 방문처리
        if(graph[nx][ny] == 1):
          queue.append((nx, ny))
          graph[nx][ny] = 0

t = int(input())  # 테스트 케이스 수

for _ in range(t):
  # 가로, 세로, 배추 개수
  m, n, k = map(int, input().split())
  # 0: 땅, 1: 배추
  graph = [[0] * m for _ in range(n)]
  res = 0  # 지렁이 수
  
  for i in range(k):
    y, x = map(int, input().split())
    graph[x][y] = 1  # 배추 표시

  # 탐색
  for i in range(n):
    for j in range(m):
      # 배추이면
      if graph[i][j] == 1:
        bfs(i, j)
        res += 1  # 지렁이 개수 1증가
  print(res)

'''
import sys
sys.setrecursionlimit(10**6)  # 최대 재귀 깊이 설정

t = int(input())  # 테스트 케이스 수
# 위치벡터(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS
def dfs(x, y):
  # 현재 좌표 방문 처리
  graph[x][y] = 0

  # 상하좌우 탐색
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # 좌표 범위 내이면
    if(0 <= nx < n and 0 <= ny < m):
      # 배추이면 재귀 호출
      if(graph[nx][ny] == 1):
        dfs(nx, ny)
  return 0

for _ in range(t):
  # 가로, 세로, 배추 개수
  m, n, k = map(int, input().split())
  # 0: 땅, 1: 배추
  graph = [[0] * m for _ in range(n)]
  res = 0  # 지렁이 수
  
  for i in range(k):
    y, x = map(int, input().split())
    graph[x][y] = 1  # 배추 표시

  # 탐색
  for i in range(n):
    for j in range(m):
      # 배추이면
      if graph[i][j] == 1:
        dfs(i, j)
        res += 1  # 지렁이 개수 1증가
  print(res)
  

'''
