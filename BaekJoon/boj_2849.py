n = int(input())  # 10**18 이하의 자연수
k = 10**6  # 피보나치 수를 나눌 값
# k = 10**n이면, p = 15*10**(n-1)
p = 15 * 10**5  # 피노사 주기

n %= p  # 우리가 구해야할 값
a, b = 0, 1  # 피보나치 수를 기록할 dp 테이블
for i in range(n - 1):
  a, b = b % k, (a + b) % k
print(b)