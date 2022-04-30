import sys
input = sys.stdin.readline

# DFS(깊이, 비용)
def dfs(depth, cost):
  global min_cost
  # n개를 다 선택하면
  if depth == n:
    # 마지막 도시->시작 도시로 갈 수 있다면
    if graph[temp[n - 1]][temp[0]] != 0:
      min_cost = min(min_cost, cost + graph[temp[n - 1]][temp[0]])  # 최솟값 갱신
    return
  
  # 1~n 도시 선택하기(순열)
  for i in range(n):
    # 1. 첫번째 도시이거나
    # 2. 이전에 방문한적이 없고 해당 도시로 이동할 수 있고 최소 비용보다 작다면
    if depth == 0 or (not visited[i] and graph[temp[depth - 1]][i] != 0 and min_cost > cost):
      temp.append(i)      # i번 도시 선택
      visited[i] = True   # i번 도시 방문 처리
      # 현재 도시->선택 도시 비용을 더해서 넘겨줌
      dfs(depth + 1, cost + graph[temp[depth - 1]][i])
      temp.pop()          # i번 도시 선택 해제(원상복귀)
      visited[i] = False  # i번 도시 방문 처리 해제

n = int(input())  # 도시 수
# n개의 비용(도시 i->j로 가기위한 비용)
graph = [list(map(int, input().split())) for _ in range(n)]
temp = []       # 이동 경로
min_cost = 1e9  # 최소 비용
visited = [False for _ in range(n)]  # 방문 여부

dfs(0, 0) 
print(min_cost)
