import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 세로, 가로
# n * m(W: 흰색, B: 검정색)
graph = [list(input().strip()) for _ in range(n)]
min_cnt = 1e9  # 다시 칠해야 하는 칸의 최솟값

# 입력받은 2차원 리스트에서 8 * 8 2차원 리스트 추출해서 검사
for i in range(n - 7):
  for j in range(m - 7):
    # 8 * 8 추출하기
    board = [row[j: j + 8] for row in graph[i: i + 8]] 
    cntB, cntW = 0, 0  # 다시 칠해야하는 정사각형 개수
    for r in range(8):
      for c in range(8):
        # 짝수행, 짝수열 혹은 홀수행, 홀수열
        if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 1 and c % 2 == 1):
          # 검정색으로 칠하기
          if board[r][c] == 'W':  cntB += 1
          # 흰색으로 칠하기
          else: cntW += 1
        # 짝수행, 홀수열 혹은 홀수행, 짝수열
        else:
          # 흰색으로 칠하기
          if board[r][c] == 'B':  cntB += 1
          # 검정색으로 칠하기
          else:  cntW += 1
    min_cnt = min(min_cnt, cntB, cntW)
print(min_cnt)