from collections import deque

# 가로, 세로, 높이
m, n, h = map(int, input().split())
# 0: 안익음, 1: 익음, -1: 빈칸(3차원 리스트)
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)] 
target = []  # 익은 토마토 위치
num = 0  # 안익은 토마토 개수

# 위,아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

# BFS
def bfs(target):
  queue = deque()
  # 시작 좌표들 삽입
  for i in target:
    queue.append(i)

  while queue:
    z, x, y = queue.popleft()
    # 6가지 방향 탐색
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      # 범위 내이고 익지 않은 토마토라면
      if(0 <= nz < h and 0 <= nx < n and 0 <= ny < m):
        if(graph[nz][nx][ny] == 0):
          # 삽입, 방문처리
          queue.append((nz, nx, ny))
          graph[nz][nx][ny] = graph[z][x][y] + 1


# 익은 토마토 좌표 찾기
for i in range(h):
  for j in range(n):
    for k in range(m):
      # 익은 토마토라면
      if(graph[i][j][k] == 1): 
        target.append((i, j, k))
      # 익지 않은 토마토라면
      elif(graph[i][j][k] == 0):
        num += 1  

# 1. 저장될 때부터 모든 토마토가 익었으면(0이 없으면)
if(num == 0):
  print(0)
else:
  bfs(target)
  
  for i in range(h):
    for j in range(n):
      # 2. 토마토가 모두 익지 못한다면(0이 있으면)  
      if(0 in graph[i][j]):
        print(-1)
        exit()
  
  # 3. 토마토가 모두 익었다면(0이 없으면)
  max = 0
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if(graph[i][j][k] > max):
          max = graph[i][j][k]
  print(max - 1)