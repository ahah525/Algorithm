x = int(input()) 
d = [0] * (30001)  # dp 테이블 초기화

# bottom-up
for i in range(2, x + 1):
  # 4. x에서 1을 뺌
  d[i] = d[i - 1] + 1
  # 3. x가 2의 배수이면 2로 나눔
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  # 2. x가 3의 배수이면 3으로 나눔
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  # 1. x가 5의 배수이면 5로 나눔
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[x])  # x에서 1을 만드는 최소 연산 횟수