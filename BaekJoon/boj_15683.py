from copy import deepcopy
import sys
input = sys.stdin.readline

# DFS
def dfs(graph, depth):
  global k, min_blind  
  temp = deepcopy(graph)  # 깊은 복사
  # 모든 CCTV 방향이 설정되었다면
  if depth == k:
    blind = 0  # 사각지대 개수
    # 사각지대 개수 세기
    for i in range(n):
      blind += temp[i].count(0)
    min_blind = min(min_blind, blind)  # 최솟값 업데이트
    return

  x, y, cctv_num = cctv[depth]  # 좌표, cctv 번호
  # 해당 cctv 번호의 방법들에 대해 반복
  for way in dir[cctv_num]:
    # 1. 해당 cctv 번호의 방법에 대한 방향으로 이동
    for d in way:
      nx, ny = x, y  # 이동해야할 좌표
      while True:
        # 해당 방향으로 계속 직진
        nx += dx[d]
        ny += dy[d]
        # 범위 내이고
        if 0 <= nx < n and 0 <= ny < m:
          # 빈칸이면 체크하기
          if temp[nx][ny] == 0:  temp[nx][ny] = '#'
          # 벽이면 탈출
          elif temp[nx][ny] == 6:  break
        # 범위 밖이면 탈출
        else:  break
    # 2. dfs 호출
    dfs(temp, depth + 1)
    # 3. dfs 전으로 원상복귀
    temp = deepcopy(graph)  

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# CCTV 방향(1~5)
dir = [
  [],
  [[0], [1], [2], [3]],
  [[0, 2], [1, 3]],
  [[0, 1], [1, 2], [2, 3], [3, 0]],
  [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
  [[0, 1, 2, 3]],
]
    
n, m = map(int, input().split())  # 세로, 가로
# n * m (0: 빈칸, 1~5: CCTV, 6:벽)
graph = [list(map(int, input().split())) for _ in range(n)]
min_blind = 1e9  # 사각지대 최소 크기
cctv = []  # cctv 좌표, 번호 목록
k = 0      # cctv 개수
# CCTV 번호, 좌표 찾기
for i in range(n):
  for j in range(m):
    # CCTV면
    if 1 <= graph[i][j] <= 5:
      cctv.append((i, j, graph[i][j]))  # 좌표, cctv번호
      k += 1

dfs(graph, 0)
print(min_blind)
