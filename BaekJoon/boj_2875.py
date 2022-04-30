n, m, k = map(int, input().split())
team = 0  # 팀 수
 
while True:
  # 탈출 조건
  if(n < 0 or m < 0 or n + m < k):
    team -= 1  # 범위 외이므로 1개 차감
    break
  # 팀 결성
  team += 1  # 팀 수 
  n -= 2
  m -= 1
 
print(team)