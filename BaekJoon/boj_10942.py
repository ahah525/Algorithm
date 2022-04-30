import sys
input = sys.stdin.readline

n = int(input())  # 수열 크기
graph = list(map(int, input().split()))  # 크기가 n인 수열
m = int(input())  # 질문 개수
# d[i][j]: i~j번째까지 수의 펠린드롬 여부(1: 펠린드롬, 0: 아님)
d = [[0] * n for _ in range(n)]

for k in range(n):
  for i in range(n - k):
    j = i + k
    # 1. 원소가 1개면 항상 팰린드롬
    if i == j:
      d[i][j] = 1
    # 2. 원소 2개면 두 값이 같을 때만 팰린드롬
    elif j - i == 1:
      if graph[i] == graph[j]:   
        d[i][j] = 1
    # 3. 원소가 3개이상이면
    else:
      # 양쪽 끝값이 같고 가운데 부분이 펠린드롬이면 팰린드롬
      if d[i + 1][j - 1] == 1 and graph[i] == graph[j]:   
        d[i][j] = 1
    i += 1

for _ in range(m):
  s, e = map(int, input().split())  # s번째수, e번째 수
  print(d[s-1][e-1])
