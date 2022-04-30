n = int(input())  # 체스판 크기
cnt = 0  # 경우의 수
row = [0] * n  # 

# x 행에 퀸 배치하기
def dfs(x):
  global cnt  
  # n개를 다 놓았다면(n행이면) 종료
  if x == n:
    cnt += 1  # 경우의 수 1개 증가
    return
  # n개를 다 놓지 않았다면
  else:
    # y열에 퀸 배치하기
    for y in range(n):
      row[x] = y  # [x, y]에 퀸 배치
      possible = True  # 배치 가능 여부
      # x행 위쪽 검사(0 ~ x-1)
      for i in range(x):
        # 1. 같은 열에 퀸이 있으면 2. 대각선에 퀸이 있으면
        if row[x] == row[i] or abs(x - i) == abs(row[x] - row[i]):
          possible = False
          break
      if possible:  dfs(x + 1)  # 다음 행 배치하기

dfs(0)  # 0행부터 배치 시작
print(cnt)
  