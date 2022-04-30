import sys

# DFS
def dfs(depth):
  global find
  # 정답 찾았으면 종료
  if find:  return
  # 빈 칸을 다 채우면
  if depth == blank_num:
    for i in graph:
      print(*i)
    find = True  # 정답 찾음으로 변경
    return
  # 빈 칸을 다 채우지 못했으면
  x, y = blank[depth]  # depth번째 빈칸 좌표
  target = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # 넣을 수 있는 후보 숫자
  # 1. 가로줄, 세로줄에 있는 숫자 후보에서 제거
  for i in range(9):
    target.discard(graph[x][i])  # 가로줄
    target.discard(graph[i][y])  # 세로줄  
  # 2. 굵은 선 3*3 정사각형 칸에 있는 수 후보에서 제거
  for i in range(3):
    for j in range(3):
      target.discard(graph[(x // 3) * 3 + i][(y // 3) * 3 + j])   
  # 후보 숫자 중에 선택하기
  for i in target:
    graph[x][y] = i  # 선택한 숫자 쓰기
    dfs(depth + 1)
    graph[x][y] = 0  # 원상복귀

# 9 * 9 스도쿠(0: 빈칸)
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(9)] 
blank = []     # 빈칸들 좌표
blank_num = 0  # 빈칸 개수
find = False   # 정답 찾음 여부

# 빈 칸 찾기
for i in range(9):
  for j in range(9):
    # 빈칸이면 좌표 저장
    if graph[i][j] == 0:
      blank.append((i, j))
      blank_num += 1
dfs(0)

