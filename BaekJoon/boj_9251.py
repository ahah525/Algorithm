# 1. dp 테이블 2차원 리스트
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
'''
# 2. dp 테이블 1차원 리스트
a, b = input(), input()  # 알파벳 대문자로 구성된 수열 2개
lenA, lenB = len(a), len(b)
# 문자열 a의 i번째까지 문자열& 문자열 b의 j번째까지 문자열의 LCS 길이
d = [0] * (lenB + 1)  # 문자열 b의 길이만큼 생성

# 문자열 a의 길이만큼 d 업뎃
for i in range(1, lenA + 1):
  cnt = 0  
  for j in range(1, lenB +1):
    # 누적 변수가 캐시값보다 작은 경우
    if cnt < d[j]:
      cnt = d[j]
    # 같은 글자인 경우
    elif a[i - 1] == b[j - 1]:
      d[j] = cnt + 1
  #print(d)
print(max(d))  # 두 문자열의 LCS 길이
'''