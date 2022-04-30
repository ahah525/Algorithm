import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 물품 수, 버틸 수 있는 무게
# n개의 물건 정보(무게, 가치)
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * (k + 1) for _ in range(n + 1)]

# 가방에 담을 수 있는 물건의 개수를 1부터 n까지 
for i in range(1, n + 1):
  w, v = graph[i - 1]  # 현재 물건의 무게, 가치
  # 가방의 수용 가능 무게를 1부터 k까지
  for j in range(1, k + 1):
    # 1. 현재 물건이 가방의 수용 가능 무게보다 작거나 같으면 
    if w <= j:
      # 현재 물건을 넣었을 때와 넣지 않았을 때 가치 비교
      d[i][j] = max(d[i - 1][j - w] + v, d[i - 1][j])
    # 2. 현재 물건이 가방의 수용 가능 무게보다 크면 못담음
    else:
      d[i][j] = d[i - 1][j]
print(d[n][k])  # 물건 n개에서 무게 k를 넘지 않는 가치합의 최댓값