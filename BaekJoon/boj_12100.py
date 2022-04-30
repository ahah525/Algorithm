from copy import deepcopy
import sys
input = sys.stdin.readline

# 방향에 따라 움직이는 함수
def move(d, temp):
  # 1. 위쪽으로 이동
  if d == 0:     
    # 한 열씩 위쪽으로 이동
    for y in range(n):  # 열
      idx = 0  # 이전 값(행) 인덱스
      for x in range(1, n):
        # 00. 현재값이 0이면 건너뛰기
        # 01. 현재 값이 0이 아니라면
        if temp[x][y]:
          # 현재값을 복사해 놓고 0으로 만듬
          cur = temp[x][y]   
          temp[x][y] = 0
          # 1. 이전 값이 0이라면
          if temp[idx][y] == 0:
            # 이전 값에 현재값을 대입, 이전 값은 그대로
            temp[idx][y] = cur
          # 2. 이전 값과 현재값이 같다면
          elif temp[idx][y] == cur:
            # 이전 값에 현재값을 더해줌, 이전 값 바꿈
            temp[idx][y] *= 2
            idx += 1           
          # 3. 이전 값과 현재값이 다르다면
          else:
            # 이전 값 바꿈, 이전 값에 현재값을 대입
            idx += 1
            temp[idx][y] = cur
  # 2. 아래쪽으로 이동
  elif d == 1:     
    # 한 열씩 아래쪽으로 이동
    for y in range(n):  # 열
      idx = n - 1  # 이전 값(행) 인덱스
      for x in range(n - 2, -1, -1):
        # 00. 현재값이 0이면 건너뛰기
        # 01. 현재 값이 0이 아니라면
        if temp[x][y]:
          # 현재값을 복사해 놓고 0으로 만듬
          cur = temp[x][y]   
          temp[x][y] = 0
          # 1. 이전 값이 0이라면
          if temp[idx][y] == 0:
            # 이전 값에 현재값을 대입, 이전 값은 그대로
            temp[idx][y] = cur
          # 2. 이전 값과 현재값이 같다면
          elif temp[idx][y] == cur:
            # 이전 값에 현재값을 더해줌, 이전 값 바꿈
            temp[idx][y] *= 2
            idx -= 1           
          # 3. 이전 값과 현재값이 다르다면
          else:
            # 이전 값 바꿈, 이전 값에 현재값을 대입
            idx -= 1
            temp[idx][y] = cur
  # 3. 왼쪽으로 이동
  elif d == 2:     
    # 한 행씩 왼쪽으로 이동
    for x in range(n):  # 행
      idx = 0  # 이전 값(열) 인덱스
      for y in range(1, n):
        # 00. 현재값이 0이면 건너뛰기
        # 01. 현재 값이 0이 아니라면
        if temp[x][y]:
          # 현재값을 복사해 놓고 0으로 만듬
          cur = temp[x][y]   
          temp[x][y] = 0
          # 1. 이전 값이 0이라면
          if temp[x][idx] == 0:
            # 이전 값에 현재값을 대입, 이전 값은 그대로
            temp[x][idx] = cur
          # 2. 이전 값과 현재값이 같다면
          elif temp[x][idx] == cur:
            # 이전 값에 현재값을 더해줌, 이전 값 바꿈
            temp[x][idx] *= 2
            idx += 1           
          # 3. 이전 값과 현재값이 다르다면
          else:
            # 이전 값 바꿈, 이전 값에 현재값을 대입
            idx += 1
            temp[x][idx] = cur
  # 4. 오른쪽으로 이동
  elif d == 3:     
    # 한 행씩 오른쪽으로 이동
    for x in range(n):  # 행
      idx = n - 1  # 이전 값(열) 인덱스
      for y in range(n - 2, -1, -1):
        # 00. 현재값이 0이면 건너뛰기
        # 01. 현재 값이 0이 아니라면
        if temp[x][y]:
          # 현재값을 복사해 놓고 0으로 만듬
          cur = temp[x][y]   
          temp[x][y] = 0
          # 1. 이전 값이 0이라면
          if temp[x][idx] == 0:
            # 이전 값에 현재값을 대입, 이전 값은 그대로
            temp[x][idx] = cur
          # 2. 이전 값과 현재값이 같다면
          elif temp[x][idx] == cur:
            # 이전 값에 현재값을 더해줌, 이전 값 바꿈
            temp[x][idx] *= 2
            idx -= 1           
          # 3. 이전 값과 현재값이 다르다면
          else:
            # 0으로 바꿨던 현재값을 원래대로 바꿈, 이전 값 바꿈
            idx -= 1
            temp[x][idx] = cur

# DFS
def dfs(depth, graph):
  global max_block
  # 5번 움직였으면 종료
  if depth == 5:
    block = max(map(max, graph))
    max_block = max(max_block, block)  # 최댓값 갱신
    return
  temp = deepcopy(graph)    # 기존 graph 깊은 복사
  # 이동할 방향 설정(중복 순열)에 따라 이동
  for d in range(4):
    move(d, temp)
    dfs(depth + 1, temp)
    temp = deepcopy(graph)
    
n = int(input())  # 보드 크기
# n * n(0: 빈칸)
graph = [list(map(int, input().split())) for _ in range(n)]
max_block = 0  # 블록의 최댓값
# 상, 하, 좌, 우
dx = [ -1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, graph)
print(max_block)
