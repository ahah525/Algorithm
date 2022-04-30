# 현재 깊이, 위치
def dfs(depth, idx):
  # 깊이가 6이 되면(종료 조건)
  if depth == 6:
    print(*res)
    return
    
  # 집합에서 탐색
  for i in range(idx, k):
    res.append(s[i])  # 집합 원소 삽입
    dfs(depth + 1, i + 1)
    res.pop()         # 맨 마지막 원소 빼기
    

while True:
  t = list(map(int, input().split()))
  k = t[0]  # 집합 원소 수
  # 종료 조건
  if(k == 0):
    break
  s = t[1 :]  # 집합
  res = []  # 결과를 담을 집합
  
  dfs(0, 0)
  print()

'''
from itertools import combinations

while True:
  t = list(map(int, input().split()))
  k = t[0]  # 집합 원소 수
  # 종료 조건
  if(k == 0):
    break
  s = t[1 : len(t)]  # 집합
  for i in list(combinations(s, 6)):
    print(" ".join(map(str, i)))
  print()
'''


    