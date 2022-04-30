import sys
input = sys.stdin.readline

t = int(input())  # 테스트 케이스 수
for _ in range(t):
  k = int(input())  # 소설의 장 수(3이상 500이하)
  f = list(map(int, input().split()))  # k개의 파일 크기
  
  # i에서 j까지 합하는데 필요한 최소 비용
  d = [[0] * k for _ in range(k)]
  # 1. i에서 j까지 누적합 구하기(대각선으로 진행)
  for i in range(k - 1):
    # 각 행의 첫번째 값은 i ~ (i+1)의 합으로 초기화
    d[i][i + 1] = f[i] + f[i + 1]
    # i ~ j의 누적합
    for j in range(i + 2, k):
      d[i][j] = d[i][j - 1] + f[j]

  # (k-2)번 대각선으로 최솟값 구하기
  for n in range(2, k):
    for i in range(k - n):
      j = i + n
      # (i ~ x)의 최소 비용 + (i+1 ~ j)의 최소 비용 들 중에 최솟값
      costs = [d[i][x] + d[x + 1][j] for x in range(i, j)]
      d[i][j] += min(costs)

  print(d[0][k - 1])  # 모든 장을 합치는데 필요한 최소 비용



