n = int(input())  # 1이상 10**6이하 정수
d = [0] * (n + 1)  # i를 만들기 위한 최소 연산 사용 횟수

for i in range(2, n + 1):
  # 1. 1을 더하기
  d[i] = d[i - 1] + 1
  # 2. 2를 곱하기
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1)
  # 3. 3을 곱하기
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3] + 1)
  '''
  a = d[i-1] + 1
  b, c = a, a
  if i % 2 == 0:  b = d[i//2] + 1
  if i % 3 == 0:  c = d[i//3] + 1
  d[i] = min(a, b, c)
  '''
print(d[n])  # n을 만드는데 필요한 연산 최소 횟수
