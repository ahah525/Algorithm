from itertools import permutations

n = int(input()) 
arr = list(map(int, input().split()))  # n개의 정수
max_res = 0  # 최댓값

for a in permutations(arr):
  res = 0 
  for j in range(len(a) - 1):
      res += abs(a[j] - a[j + 1])
  if(max_res < res): max_res = res

print(max_res)
'''
n = int(input()) 
arr = list(map(int, input().split()))  # n개의 정수
max_res = 0  # 최댓값
temp = []    # 순열을 담을 곳
check = [False] * (n + 1)   # 선택 여부  

# DFS
def dfs(depth):
  global max_res
  # 깊이가 n이 되면 값 계산 후 종료
  if depth == n:
    res = 0
    for i in range(depth - 1):
      res += abs(temp[i] - temp[i + 1])
    if res > max_res:  max_res = res    
    return
  # 깊이가 n이 안됬으면
  else:
    for i in range(len(arr)):
      # i번째 인덱스 값이 아직 선택하지 않았다면
      if not check[i]:
        check[i] = True  # 선택 체크  
        temp.append(arr[i])  
        dfs(depth + 1)
        check[i] = False # 선택 해제
        temp.pop()
    
dfs(0)
print(max_res)
'''