# 중복 조합
n, m = map(int, input().split())   
temp = []  # 수열을 담을 곳
 
# DFS(깊이, 탐색시작값)
def dfs(depth, idx):
  # 길이가 m이 되었다면
  if depth == m:
    print(*temp)
    return
  # 1 ~ n 중에서 1개 뽑기
  for i in range(idx, n + 1):
    temp.append(i)
    dfs(depth + 1, i)  # 탐색 시작값은 그대로 넘겨줌
    temp.pop()
dfs(0, 1)
