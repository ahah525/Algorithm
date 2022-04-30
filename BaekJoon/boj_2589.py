from collections import deque

# BFS 
def bfs(x, y):
  visited = [[0] * m for _ in range(n)]
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < m):
        # 육지이고 방문하지 않은 곳이면 삽입, 방문 처리
        if(graph[nx][ny] == 'L' and visited[nx][ny] == 0):
          queue.append((nx, ny))
          visited[nx][ny] = visited[x][y] + 1
  return max(map(max, visited)) - 1  # 최단 거리

n, m = map(int, input().split())  # 세로, 가로
# L: 육지, W: 바다 
graph = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_time = 0
for i in range(n):
  for j in range(m):
    # 육지이면
    if(graph[i][j] == 'L'):
      min_time = max(bfs(i, j), min_time)
print(min_time)
      