import sys
input = sys.stdin.readline

n = int(input())  # 행렬의 개수(1이상 500이하)
# n개의 행렬 크기(r, c)
graph = [list(map(int, input().split())) for _ in range(n)]

# i에서 j까지 행렬을 곱하는 데 필요한 곱셈 연산의 최솟값
d = [[0] * n for _ in range(n)]

# (n-1)번 대각선으로 
for k in range(n-1): 
  for i in range(n-k-1):
    j = i + k + 1
    # 2. 두번째 대각선 이후 경우
    if k != 0:
      # i~x, x+1~j 케이스들의 최소 연산 횟수 중 최솟값 대입
      cnt = [d[i][x] + d[x+1][j] + graph[i][0] * graph[x][1] * graph[j][1] for x in range(i, j)]
      d[i][j] = min(cnt)
    # 1. 첫번째 대각선의 경우
    else:
      # 두 행렬의 곱셈 연산 횟수로 초기화
      d[i][j] = graph[i][0] * graph[i][1] * graph[j][1]

print(d[0][n-1])  # 0~(n-1)번째 행렬을 곱하는 최소 연산 횟수
  