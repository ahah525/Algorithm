n, m = map(int, input().split())  # 화폐 종류, 목표금액
graph = [int(input()) for _ in range(n)]  # n개의 화폐 가치
graph.sort()  # 오름차순 정렬
d = [10001] * (m + 1)  # 최소한의 화폐 개수
d[0] = 0  # 0원을 만들기 위해 필요한 화폐 개수는 0

# n개의 화폐 단위에 대하여
for i in range(n):
  # price를 만들기 위한 최소 화폐 개수 구하기
  for price in range(graph[i], m + 1):
    # (price - 화폐단위)를 만드는 방법이 있으면
    if d[price - graph[i]] != 10001:    
      d[price] = min(d[price], d[price - graph[i]] + 1)

if d[m] == 10001:  print(-1)
else:  print(d[m])
    
  