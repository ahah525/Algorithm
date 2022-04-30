n = int(input())  # 삼각형 크기(1이상 500이하)
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  # 행의 크기만큼 반복
  for j in range(i + 1):
    # 왼쪽 대각선 값
    if j - 1 < 0: left_up = 0
    else:  left_up = d[i - 1][j - 1]
    # 오른쪽 대각선 값
    if j >= i: right_up = 0
    else:  right_up = d[i - 1][j]
    # 왼쪽 대각선 값&오른쪽 대각선 값 중 큰 값 선택
    d[i][j] += max(left_up, right_up) 
    
for i in d:
  print(i)
print(max(d[n - 1]))  # 합이 최대가되는 경로에 있는 수의 합