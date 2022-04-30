def w(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  if a > 20 or b > 20 or c > 20:
    return w(20, 20, 20)
  # 기록된 값이 있다면 바로 리턴
  if d[a][b][c]:  return d[a][b][c]
  # 기록된 값이 없다면 계산
  if a < b < c:
    d[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    return d[a][b][c]
  else:
    d[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return d[a][b][c]

d = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
  a, b, c = map(int, input().split())  # - 50이상 50이하
  # 종료 조건
  if a == -1 and b == -1 and c == -1:  break
  # w(a, b, c) 값을 기록하기 위한 dp 테이블
  
  res = w(a, b, c)
  print(f'w({a}, {b}, {c}) = {res}')
