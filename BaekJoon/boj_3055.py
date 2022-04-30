from collections import deque
import sys
input = sys.stdin.readline

# BFS
def bfs():
  while True:
    # 1. 고슴도치 이동
    for i in range(len(queueS)):
      x, y = queueS.popleft()
      # 혹시 물로 변한 것이면 다음 위치 검사
      if(graph[x][y] == '*'):
        continue
      for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        # 범위 내이고
        if(0 <= nx < r and 0 <= ny < c):
          # 빈 곳이면 삽입, 방문 처리
          if(graph[nx][ny] == '.'):
            queueS.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
          # 비버굴(목표점)이면 바로 값 리턴
          elif(graph[nx][ny] == 'D'):
            return graph[x][y] + 1
    # 2. 물 이동
    for i in range(len(queueW)):
      x, y = queueW.popleft()
      for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        # 범위 내이고
        if(0 <= nx < r and 0 <= ny < c):
          # 빈곳 혹은 고슴도치가 지나갔던 곳이면 삽입, 방문 처리
          if(graph[nx][ny] == '.' or type(graph[nx][ny]) is int):
            queueW.append((nx, ny))
            graph[nx][ny] = '*'
    '''
    # 1분 지난 후 고슴도치, 물 이동 결과
    for i in graph:
      print(i)
    print()
    '''
    # 꺼낼 고슴도치가 없으면
    if not queueS:  return "KAKTUS"

r, c = map(int, input().split())
# r*c (.: 빈 곳, *: 물, X: 돌, D: 비버 굴, S: 고슴도치)
graph = [list(input().strip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dLoc = [0, 0]     # 비버 굴
queueW = deque()  # 물
queueS = deque()  # 고슴도치
#visited = [[0] * c for _ in range(r)]

# 고슴도치(S)와 물(*) 위치 찾기
for i in range(r):
  for j in range(c):
    # 비버 굴이면 
    if(graph[i][j] == "D"):
      dLoc = [i, j]
    # 고슴도치면 삽입, 방문 처리
    elif(graph[i][j] == 'S'):
      queueS.append((i, j))
      graph[i][j] = 0
    # 물이면 삽입
    elif(graph[i][j] == "*"):
      queueW.append((i, j))
      #visited[i][j] = 1
  
print(bfs())

