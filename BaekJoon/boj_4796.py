i = 0     # 인덱스

while True:
  i += 1
  l, p, v = map(int, input().split())
  # 탈출 조건(입력 종료)
  if(l == 0 and p == 0 and v == 0):
    break

  # 최대 캠핑장 사용일 수 계산
  res = (v // p) * l
  res += min(v % p, l) # 남은 일 수에 대한 조건 처리
  print(f"Case {i}: {res}")

