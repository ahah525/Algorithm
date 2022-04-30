import sys
from collections import deque
input = sys.stdin.readline

# BFS
def bfs(x, y):
  queue = deque()
  # 시작점 삽입, 방문 처리
  queue.append((x, y))
  visited[x][y] = 1                                                         
  while queue:
    x, y = queue.popleft()
    cnt = 0  # 현재좌표 기준 빙산 개수
    # 빙산이면 상하좌우 탐색
    if(graph[x][y] != 0):
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내이면
        if(0 <= nx < n and 0 <= ny < m):
          # 바다 개수 카운트
          if(graph[nx][ny] == 0):
            cnt += 1
          # 빙산이고 방문한적이 없으면 삽입, 방문 처리
          if(visited[nx][ny] == 0):
            queue.append((nx, ny))
            visited[nx][ny] = 1
      # 바다개수만큼 빙산 녹이기한 결과값 기록
      result[x][y] = max(graph[x][y] - cnt, 0)  # 최솟값은 0

n, m = map(int, input().split())  # 세로, 가로
# n * m (0: 바다, 1~10: 빙산)
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0  # 빙산 분리 시간

while True:
  visited = [[0] * m for _ in range(n)] # 방문 여부
  result = [[0] * m for _ in range(n)]  # 빙산이 녹은 결과
  cnt = 0     # 빙산 덩어리 개수
  melt = True # 빙산이 다 녹았는지 여부
  # 빙산 녹이기 1번(가장자리는 무조건 0이므로 검사X)
  for i in range(1, n):
    for j in range(1, m):
      # 방문하지 않은 빙산이면
      if(graph[i][j] != 0 and visited[i][j] == 0):
        bfs(i, j)
        cnt += 1      # 빙산 덩어리 개수 세기
        melt = False  # 녹지 않은 빙산 있음
  # 빙산이 다 녹았다면 0 출력
  if melt:
    print(0)
    break
  # 이전 빙산이 2개이상이었으면 분리 시간 출력
  if(cnt >= 2):  
    print(time)
    break
  # 빙산 녹이기 결과 업데이트
  graph = list(result)
  time += 1  # 분리 시간 증가