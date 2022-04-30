n, m = map(int, input().split())  # 세로, 가로
graph = [list(map(int, input())) for _ in range(n)]  # n * m
res = 0  # 아이스크림 개수

def dfs(x, y):
  # 인덱스 범위 벗어나면(종료 조건)
  if(x < 0 or x >= n or y < 0 or y >= m):
    return False

  # 현재 좌표를 아직 방문하지 않았다면
  if graph[x][y] == 0:
  	# 1.방문 처리
    graph[x][y] = 1  
    # 2. 상, 하, 좌, 우 재귀 호출로 탐색
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False

for i in range(n):
  for j in range(m):
    # 현재 위치에서 dfs 수행이 끝나면
    if dfs(i, j) == True:
      res += 1
      
print(res)