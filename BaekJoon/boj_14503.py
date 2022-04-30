from collections import deque

n, m = map(int, input().split())  # 세로, 가로
# d(0: 북, 1: 동, 2: 남, 3: 서)
r, c, d = map(int, input().split())  # 현재 좌표, 방향
# 0: 빈 칸, 1: 벽, 2: 청소한 칸
graph = [list(map(int, input().split())) for _ in range(n)]
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
def bfs(x, y, d):
  res = 0  # 청소한 칸 개수
  queue = deque()
  
  # 시작 위치 삽입, 방문 처리
  queue.append((x, y, d))  
  graph[x][y] = 2  # 방문 처리(청소)
  res += 1    # 청소 칸 개수 1증가
  
  while queue:
    x, y, d = queue.popleft()
    temp_d = d  # 원래 d값 보존을 위해 사용 
    turn = 0    # 연속 회전 횟수
    for i in range(4):
      #nd = ((d + 3) % 4 - i + 4) % 4
      # 현재 좌표&방향 기준 왼쪽 방향&좌표
      nd = (temp_d + 3) % 4
      nx = x + dx[nd]
      ny = y + dy[nd]
      temp_d = nd  # 왼쪽으로 회전한 방향 업데이트

      # 범위 내이고
      if(0 <= nx < n and 0 <= ny < m):
        # a. 청소하지 않은 곳(빈칸)이면
        if(graph[nx][ny] == 0):
          queue.append((nx, ny, nd))  # 삽입(전진)
          graph[nx][ny] = 2  # 방문 처리(청소)
          res += 1  # 청소 칸 개수 1증가
          break  # 1칸 전진한 칸에서 다시 검사하기 위해
        # 벽이나 청소한 칸이면
        else: 
          turn += 1  # 회전 횟수 1 증가
    if(turn == 4):  
      bx = x + dx[(d + 2) % 4] 
      by = y + dy[(d + 2) % 4]
      # d. 4방향 모두 청소가 되있거나 벽이면서 뒤쪽 방향이 벽이라 후진 불가능한 경우 (종료 조건)
      if(graph[bx][by] == 1):
        return res
      # c. 4방향 모두 청소가 되있거나 벽인 경우 
      queue.append((bx, by, d))  # 삽입(후진)

# 현재 위치, 방향에서 호출
print(bfs(r, c, d))
