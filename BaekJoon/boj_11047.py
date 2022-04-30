n, k = map(int, input().split())  # 동전 종류 수, 총 금액
coins = [int(input()) for _ in range(n)] # 동전 가치(오름차순)
coins.sort(reverse=True)  #  내림차순 정렬
cnt = 0  # 필요한 동전 개수

# 필요한 동전 개수 최솟값 찾기
for coin in coins:
  # 모두 잔액이 처리되면 탈출
  if(k == 0):
    break
  # 동전 가치가 금액보다 작거나 같으면
  if(coin <= k):
    n = (k // coin)  # 동전 종류 k로 바꿀 수 있는 최대 개수 
    k -= (coin * n)  # 잔액 변경
    cnt += n         # 개수 추가

print(cnt)
    



