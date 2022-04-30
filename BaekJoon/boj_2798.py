from itertools import combinations

# n: 카드 개수,m: 기준 숫자
n, m = map(int, input().split())
card = list(map(int, input().split()))  # n장의 카드
max_res = 0  # M에 최대한 가까운 카드 3장의 합
res = 0

# n개에서 3장 뽑아 m에 가장 가까운 3장의 합 찾기
for c in list(combinations(card, 3)):
  res = sum(c)
  if(res <= m and max_res < res):
    max_res = res
print(max_res)

'''
for i in range(0, n - 2):
  for j in range(i + 1, n - 1):
    for k in range(j + 1, n):
      res = card[i] + card[j] + card[k]
      if(res <= m and max_res < res):
        max_res = res
'''

