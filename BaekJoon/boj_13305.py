n = int(input())  # 도시 수
distance = list(map(int, input().split()))  # 도시 간 거리(n-1 개)
price = list(map(int, input().split()))  # 리터당 가격(n 개)

cost = 0     # 총 비용
target = 1e9 # 현재까지 최소 가격
for i in range(n-1):
  # 현재 가격이 현재까지 최소 가격이 보다 작으면
  if(target > price[i]):
    # 최소 가격 갱신
    target = price[i]
  cost += distance[i] * target  # 최소 가격으로 계산
    
print(cost)
