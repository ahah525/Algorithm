import sys
sys.setrecursionlimit(10**6)  # 최대 재귀 깊이 설정
input = sys.stdin.readline

def dfs(x, y):
  '''
  # dp 기록 과정 확인 
  for i in d:
    print(i)
  print()
  '''
  # 도착점이면 경우의 수 1개 리턴
  if x == n - 1 and y == m - 1:
    return 1
  # (x, y)에서 도착점까지 가는 경우의 수를 이미 구했으면
  if d[x][y] != -1:
    return d[x][y]  # 바로 리턴
  # (x, y)에서 도착점까지 가는 경우의 수를 아직 구하지 않았으면
  d[x][y] = 0  # 방문 처리(경우의 수를 0으로 초기화)
  
  # 상하좌우 탐색
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 탐색할 좌표가 범위내 이면
    if 0 <= nx < n and 0 <= ny < m:
      # 탐색할 지점이 현재 지점보다 더 낮은 곳이면 이동
      if graph[nx][ny] < graph[x][y]:
        d[x][y] += dfs(nx, ny)  
  return d[x][y]

n, m = map(int, input().split())  # 세로, 가로
# n * m 의 높이 정보
graph = [list(map(int, input().split())) for _ in range(n)]
# (i, j)에서 출발해서 (n-1, m-1)까지 가는 경우의 수
d = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))  # 이동 가능한 경로의 수
    