s = input().split("-")  # - 기준 분리
res = 0    # 최솟값

# 첫번째 괄호의 합 - (나머지 괄호의 합)
n = list(map(int, s[0].split("+")))
res += sum(n)  # 첫번째 괄호의 합

for i in s[1:]:
  n = list(map(int, i.split("+")))
  res -= sum(n)  # 나머지 괄호들의 합 빼기

print(res)  
