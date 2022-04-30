n = list(input()) 
n.sort(reverse=True)  # 내림차순 정렬
sum = 0  # 자리수들의 합

# 자리수 합 구하기
for i in n:
  sum += int(i)

# 자리수의 합이 3의 배수이고, 일의 자리수가 0이면
if(sum % 3 == 0 and "0" in n):
  print(''.join(n))
else:
  print(-1)