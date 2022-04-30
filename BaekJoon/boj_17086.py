from collections import deque

# BFS
def bfs(sharks):
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  for i in range(len(sharks)):
    x, y = sharks[i][0], sharks[i][1]
    queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < m):
        # 빈칸이고 방문한적이 없으면
        if(graph[nx][ny] == 0):
          queue.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1
  # 최댓값 계산
  max_dis = max(map(max, graph))
  return max_dis - 1

n, m = map(int, input().split())  # 세로, 가로
# n * m (0: 빈칸, 1: 아기 상어)
graph = [list(map(int, input().split())) for _ in range(n)]
# 상하좌우 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

sharks = []  # 상어 좌표들
for i in range(n):
  for j in range(m):
    # 상어 좌표 찾기
    if(graph[i][j] == 1):
      sharks.append((i, j))
print(bfs(sharks))