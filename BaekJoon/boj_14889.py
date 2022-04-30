import sys
input = sys.stdin.readline

# DFS
# n명에서 절반 뽑기
def dfs(depth, start):
  global min_diff
  # 절반 뽑았으면
  if depth == n / 2:
    powerA, powerB, diff = 0, 0, 0 
    # A, B팀 능력치 합 구하기
    for i in range(n):
      for j in range(n):
        # 둘다 A팀이면
        if temp[i] == 0 and temp[j] == 0:  powerA += graph[i][j]
        # 둘다 B팀이면
        elif temp[i] == 1 and temp[j] == 1:  powerB += graph[i][j]
    diff = abs(powerA - powerB)    # 능력치 차이 계산
    min_diff = min(min_diff, diff)
    return

  # 팀 선택하기(조합)
  for i in range(start, n):
    temp[i] = 1  # B팀 선택
    dfs(depth + 1, i + 1)
    temp[i] = 0  # 원상복귀
          
n = int(input())  # 사람수(짝수)
# 능력치 정보(n * n)
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = 1e9  # 능력치 차이 최솟값
# (A팀: 0, B팀: 1)
temp = [0 for _ in range(n)]

dfs(0, 0)
print(min_diff)