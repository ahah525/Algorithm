from collections import deque

n, m = map(int, input().split())  # 목표 좌표
# 0: 이동 불가, 1: 이동 가능
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x, y): 
  # 시작 좌표 삽입, 방문 처리
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 1  # 갈 수 없는 길로 변경

  while queue:
    x, y = queue.popleft()

    # 상하좌우 탐색
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < m):
        # 갈 수 있는 길이면 삽입, 방문 처리
        if(graph[nx][ny] == 1):
          queue.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1 

bfs(0, 0)
print(graph[n-1][m-1])
