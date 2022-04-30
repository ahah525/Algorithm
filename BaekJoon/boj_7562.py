import sys
from collections import deque

# BFS
def bfs(x, y):
  queue = deque()
  # 시작 위치 삽입, 방문 처리
  queue.append((x, y))
  graph[x][y] = 1

  while queue:
    x, y = queue.popleft()
    # 목표 지점에 도달하면 종료
    if(x == endX and y == endY):
      break

    # 8가지 방향 탐색
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if(0 <= nx < l and 0 <= ny < l):
        # 방문하지 않은 곳이면
        if graph[nx][ny] == 0:
          # 삽입, 방문 처리
          queue.append((nx, ny))
          graph[nx][ny] = graph[x][y] + 1     
  
# 위치 벡터
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(sys.stdin.readline())  # 테스트 케이스 수
for _ in range(t):
  l = int(sys.stdin.readline())  # 체스판 길이
  startX, startY = list(map(int, sys.stdin.readline().split()))
  endX, endY = list(map(int, sys.stdin.readline().split()))
  graph = [[0] * l for _ in range(l)]  # l * l

  bfs(startX, startY)
  print(graph[endX][endY] - 1)