n, m = map(int, input().split())   
temp = []  # 수열을 담을 곳

# DFS
def dfs(depth):
  # 길이가 m이 되었다면
  if depth == m:
    print(*temp)
    return
  # 1 ~ n 중에서 1개 뽑기
  for i in range(1, n + 1):
    # 이전에 선택한 값이 아니라면
    if i not in temp:
      temp.append(i)
      dfs(depth + 1)
      temp.pop()
dfs(0)