n = int(input())  # 분해합(자연수)
res = 0  # 생성자

for i in range(1, n + 1):
  # i + i의 각 자리수의 합
  cnt = i + sum(map(int, str(i)))
  if(cnt == n):
    res = i
    break

print(res)
  
