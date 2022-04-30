t = int(input())  # 테스트 케이스 수
for _ in range(t):
  n, m = map(int, input().split())  # 세로, 가로
  array = list(map(int, input().split()))  # n * m 개의 금 개수
  d = []  # n * m(2차원 dp 테이블)
  j = 0
  for i in range(n):
    d.append(array[j:j + m])
    j += m

  # 한 열씩 진행
  for j in range(1, m):
    for i in range(n):
      # 1. 왼쪽 위에서 오는 경우
      if i == 0:  left_up = 0  # 왼쪽 위 값 없음
      else:   left_up = d[i - 1] [j - 1]  # 왼쪽 위 값
      # 2. 왼쪽에서 오는 경우
      left = d[i][j - 1]  # 왼쪽 값
      # 3. 왼쪽 아래에서 오는 경우
      if i == n - 1:  left_down = 0  # 왼쪽 아래 값 없음
      else:  left_down = d[i + 1][j - 1]  # 왼쪽 아래값

      # i행 j열까지 얻을 수 있는 금의 최댓값 계산
      d[i][j] = d[i][j] + max(left_up, left, left_down)
  res = 0  # 채굴자가 얻을 수 있는 금의 최대 크기
  for i in range(n):
    res = max(res, d[i][m - 1])
  print(d)
  print(res)
'''

t = int(input())  # 테스트 케이스 수
for _ in range(t):
  n, m = map(int, input().split())  # 세로, 가로
  graph = list(map(int, input().split()))  # n * m 개의 금 개수
  d = [0] * (n * m)  # 금의 최대 크기

  for i in range(n*m):
    # 0열 초기화
    if i % m == 0:
      d[i] = graph[i]
    # 마지막 열이 아니면
    if i % m != 3:
      # 1. 오른쪽
      if 0 <= i + 1 < n * m:
        d[i + 1] = max(d[i + 1], d[i] + graph[i + 1])
      # 2. 오른쪽 위
      if 0 <= i + 1 - m < n * m:
        d[i + 1 - m] = max(d[i + 1 - m], d[i] + graph[i + 1 - m])
      # 3. 오른쪽 아래
      if 0 <= i + 1 + m < n * m:
        d[i + 1 + m] = max(d[i + 1 + m], d[i] + graph[i + 1 + m])

  res = 0  # 채굴자가 얻을 수 있는 금의 최대 크기
  for i in range(m - 1, n*m, m):
    res = max(res, d[i])
  print(d)  
  print(res)
'''