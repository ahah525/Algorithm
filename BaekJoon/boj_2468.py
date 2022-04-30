import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DFS
def dfs(x, y, h):
  # 현재 지점 방문 처리
  visited[x][y] = 1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if(0 <= nx < n and 0 <= ny < n):
      # 방문한적이 없고 기준 높이보다 크면 
      if(visited[nx][ny] == 0 and h < graph[nx][ny]):
        visited[nx][ny] = 1  # 방문 처리
        dfs(nx, ny, h)

n = int(input())  # 행, 열 크기
# n * n 맵
graph = [list(map(int, input().split())) for _ in range(n)]
#visited = [[0] * n for _ in range(n)]
# 2차원 리스트 최솟값, 최댓값
min_h = min(map(min, graph))
max_h = max(map(max, graph))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_safe = 0  # 최대 안전 영역 수
for h in range(min_h - 1, max_h):
  visited = [[0] * n for _ in range(n)]
  safe = 0  # 안전한 영역 개수
  for i in range(n):
    for j in range(n):
      # 방문한적이 없고 기준 높이보다 크면 
      if(visited[i][j] == 0 and h < graph[i][j]):
        dfs(i, j, h)
        safe += 1  # 안전 영역 개수 1증가
  
  if(safe > max_safe): max_safe = safe

print(max_safe)


'''

from collections import deque
import sys
input = sys.stdin.readline

# BFS
def bfs(x, y, h):
  queue = deque()
  # 시작 지점 삽입, 방문 표시
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 내이이고
      if(0 <= nx < n and 0 <= ny < n):
        # 방문한적이 없고 기준 높이보다 크면 
        if(visited[nx][ny] == 0 and h < graph[nx][ny]):
          # 삽입, 방문 표시
          queue.append((nx, ny))
          visited[nx][ny] = 1

n = int(input())  # 행, 열 크기
# n * n 맵
graph = [list(map(int, input().split())) for _ in range(n)]
#visited = [[0] * n for _ in range(n)]
# 2차원 리스트 최솟값, 최댓값
min_h = min(map(min, graph))
max_h = max(map(max, graph))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_safe = 0  # 최대 안전 영역 수
for h in range(min_h - 1, max_h):
  visited = [[0] * n for _ in range(n)]
  safe = 0  # 안전한 영역 개수
  for i in range(n):
    for j in range(n):
      # 방문한적이 없고 기준 높이보다 크면 
      if(visited[i][j] == 0 and h < graph[i][j]):
        bfs(i, j, h)
        safe += 1  # 안전 영역 개수 1증가
  
  if(safe > max_safe): max_safe = safe

print(max_safe)
'''