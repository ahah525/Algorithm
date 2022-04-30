n = int(input())  # 가로 길이

d = [0] * 1001    # 바닥을 채우는 경우의 수
d[1], d[2] = 1, 3 
for i in range(3, n + 1):
  # i - 1번째까지 다 채워진 경우 2*1 1개 1가지만 가능
  # i - 2번째까지 다 채워진 경우 1*2 2개/2*2 1개 2가지만 가능
  d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])  
  
 
