from collections import deque

# BFS
def bfs(x, y):
  size = 0  # 그림 넓이
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, y))
  graph[x][y] = 2

  while queue:
    x, y = queue.popleft()
    size += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < m):
        # 방문하지 않은 곳이면 삽입, 방문 처리
        if(graph[nx][ny] == 1):
          queue.append((nx, ny))
          graph[nx][ny] = 2
  return size

n, m = map(int, input().split())  # 세로, 가로
# 0: 색칠X, 1: 색칠O
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0       # 그림 개수
max_size = 0  # 가장 큰 그림의 넓이
for i in range(n):
  for j in range(m):
    if(graph[i][j] == 1):
      max_size = max(max_size, bfs(i, j))      
      cnt += 1

print(cnt)
print(max_size)
