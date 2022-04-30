from collections import deque
import sys
input = sys.stdin.readline

# BFS
def bfs():
  
  while True:
    # 1. 지훈 1분 이동
    for i in range(len(queueJ)):
      x, y = queueJ.popleft()
      # 꺼낸 지훈의 위치값이 불(F)로 덮어쓰여졌다면 건너뛰기
      if(graph[x][y] == 'F'): continue
      for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        # 범위 내이고
        if(0 <= nx < r and 0 <= ny < c):
          # 빈 곳이면 삽입, 방문 처리
          if(graph[nx][ny] == '.'):
            queueJ.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
        # 범위 밖이면 탈출
        else: return graph[x][y] + 1
    # 2. 불 1분 이동
    for i in range(len(queueF)):
      x, y = queueF.popleft()
      for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        # 범위 내이고
        if(0 <= nx < r and 0 <= ny < c):
          # 빈 곳 혹은 지훈이 지나간 곳(숫자)이면 삽입, 방문 처리
          if(graph[nx][ny] == '.' or type(graph[nx][ny]) == int):
            queueF.append((nx, ny))
            graph[nx][ny] = 'F'
    # 더이상 꺼낼 지훈의 좌표가 없다면
    if not queueJ:  return "IMPOSSIBLE"
          
r, c = map(int, input().split())  # 세로, 가로
# r*c (.: 빈곳, #: 벽, J: 지훈, F: 불)
graph = [list(input().strip()) for _ in range(r)]
queueJ = deque()  # 지훈 위치를 담을 큐
queueF = deque()  # 불 위치를 담을 큐
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지훈, 불 시작점 위치 찾기
for i in range(r):
  for j in range(c):
    # 지훈이면 삽입, 방문 처리
    if(graph[i][j] == 'J'):
      queueJ.append((i, j))
      graph[i][j] = 0
    # 불이면 삽입(방문처리는 따로 할 필요X)
    elif(graph[i][j] == 'F'):
      queueF.append((i, j))
print(bfs())