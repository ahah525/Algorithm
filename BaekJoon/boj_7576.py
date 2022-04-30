from collections import deque

m, n = map(int, input().split())  # 가로, 세로
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 빈 칸
graph = [list(map(int, input().split())) for _ in range(n)]
target = []  # 익은 토마토 좌표들
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(target):
  # 익은 토마토가 있는 모든 좌표 삽입
  queue = deque() 
  for i in target:
    queue.append(i)

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위 내이고 익지 않은 토마토(0)이라면
      if(0 <= nx < n and 0 <= ny < m):
        if(graph[nx][ny] == 0):
          # 삽입, 방문 처리
          queue.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1  # 익은 토마토로 변환

# 1. 저장될 때 부터 모든 토마토가 익었다면(입력받은 값 중 0이 없다면)
if all(0 not in l for l in graph):
  print(0)
# 안익은 토마토가 하나라도 있다면
else:
  # 익은 토마토 좌표 구하기
  for i in range(n):
    for j in range(m):
      if(graph[i][j] == 1):
        target.append((i, j))
  # 익은 토마토들에 대해 bfs 수행
  bfs(target)
  # 2.토마토가 모두 익지 않았다면(0인 값이 1개라도 있으면)
  if any(0 in l for l in graph):
    print(-1)
  # 3. 토마토가 모두 익었다면(0인 값이 없다면)
  else:
    # 최댓값 출력()
    print(max(map(max, graph)) - 1)