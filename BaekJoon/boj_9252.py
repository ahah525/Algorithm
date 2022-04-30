# 2. dp테이블에 LCS길이 기록
a, b = input(), input()  # 알파벳 대문자로 구성된 수열 2개
lenA, lenB = len(a), len(b)
# 문자열 a의 i번째까지 문자열& 문자열 b의 j번째까지 문자열의 LCS 길이
d = [[0] * (lenB + 1) for _ in range(lenA + 1)]

for i in range(1, lenA + 1):
  for j in range(1, lenB +1):
    # 1. 두 문자열의 끝 문자가 같은 경우
    if a[i - 1] == b[j - 1]:
      d[i][j] = d[i - 1][j - 1] + 1
    # 2. 두 문자열의 끝 문자가 다른 경우
    else:
      d[i][j] = max(d[i - 1][j], d[i][j - 1])
print(d[lenA][lenB])  # 두 문자열의 LCS 길이 
      
# 두 문자열의 lcs 구하기
i, j = lenA, lenB
lcs = ""  # 두 문자열의 LCS
cnt = 0
while True:
  # 종료 조건
  if cnt == d[lenA][lenB]:
    break
  # 1. 두 문자가 같다면
  if a[i - 1] == b[j - 1]:
    lcs = a[i - 1] + lcs  # 문자를 앞에 추가  
    cnt += 1
    # 왼쪽 위 대각선으로 탐색할 인덱스 변경
    i -= 1
    j -= 1
  # 2. 두 문자가 다르다면
  else:
    # 자신과 같은 값인 곳으로 탐색할 인덱스 변경
    if d[i][j] == d[i - 1][j]:
      i -= 1  # 위쪽
    elif d[i][j] == d[i][j - 1]:
      j -= 1  # 왼쪽
if lcs != "":
  print(lcs)
'''
# 1. dp 테이블에 lcs 기록
a, b = input(), input()  # 알파벳 대문자로 구성된 수열 2개
lenA, lenB = len(a), len(b)
# 문자열 a의 i번째까지 문자열& 문자열 b의 j번째까지 문자열의 LCS 길이
d = [[""] * (lenB + 1) for _ in range(lenA + 1)]

for i in range(1, lenA + 1):
  for j in range(1, lenB + 1):
    # 1. 같은 문자면 해당 문자를 더함
    if a[i - 1] == b[j - 1]:
      d[i][j] = d[i - 1][j - 1] + a[i - 1]
    # 2. 다른 문자면 같은 값인 곳으로 이동
    else:
      if len(d[i - 1][j]) == len(d[i][j - 1]):
        d[i][j] = d[i - 1][j]
      else:
        d[i][j] = d[i][j - 1]
if d[lenA][lenB] == "":
  print(0)
else:
  print(len(d[lenA][lenB]))
  print(d[lenA][lenB])
'''