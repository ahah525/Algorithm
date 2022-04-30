n = int(input())  # 지도 크기
# n * n(0: 집이 없는 곳, 1: 집이 있는 곳)
graph = [list(map(int, input())) for _ in range(n)]
res = 0     # 총 단지 수
house = []  # 단지별 집 수
num = 0     # 집 수
# 방향 벡터(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS
def dfs(x, y):
  global num
  # 현재 노드 방문처리
  graph[x][y] = 0
  num += 1
  
  # 상하좌우 탐색
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # 좌표가 범위 이내이면
    if(0 <= nx < n and 0 <= ny < n):
      if graph[nx][ny] == 1:
        dfs(nx, ny)  # 재귀 호출

for i in range(n):  
  for j in range(n):
    # 집이 있는 곳이면
    if graph[i][j] == 1:
      dfs(i, j)  # 현재 좌표 dfs 호출
      res += 1   # 단지수 증가
      house.append(num)  # 해당 단지의 집 수 삽입
      num = 0            # 집 수 초기화  
      
print(res)
for i in sorted(house):
  print(i)

'''
from collections import deque
 
n = int(input())  # 지도 크기
# n * n(0: 집이 없는 곳, 1: 집이 있는 곳)
graph = [list(map(int, input())) for _ in range(n)]
res = 0  # 총 단지 수
house = []  # 단지별 아파트 수
 
# 방향 벡터(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
# BFS
def bfs(x, y):
  num = 0  # 집 수
  global res
  
  queue = deque()
  # 현재 노드 삽입, 방문처리
  queue.append((x, y))
  graph[x][y] = 0
 
  while queue:
    x, y = queue.popleft()  # 꺼낸 좌표
    num += 1
    # 상하좌우 탐색
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 좌표가 범위 이내이면
      if(0 <= nx < n and 0 <= ny < n):
        # 집이면 삽입, 방문처리
        if graph[nx][ny] == 1:
          queue.append((nx, ny))
          graph[nx][ny] = 0	
  house.append(num)		# 단지 내 집 수 삽입
 
for i in range(n):  
  for j in range(n):
    # 집이 있는 곳이면
    if graph[i][j] == 1:
      res += 1   # 단지수 증가
      #dfs(i, j, 0)  # 현재 좌표 dfs 호출
      bfs(i, j)
      
print(res)
# 단지 내 집 수 오름차순 출력
for i in sorted(house):
  print(i)
'''