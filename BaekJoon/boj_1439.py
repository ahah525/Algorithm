s = input()  # 0, 1로 구성된 문자열
cnt = 0      # 변화 횟수

for i in range(len(s) - 1):
  # 이전 숫자와 현재 숫자가 다를 경우
  if(s[i] != s[i+1]):
    cnt += 1  

print((cnt + 1) // 2)
