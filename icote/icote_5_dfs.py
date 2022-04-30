# DFS 메서드
def dfs(graph, v, visited):
  # 현재 노드 방문 처리
  visited[v] = True
  print(v, end=' ')

  # 현재 노드와 연결된 다른 노드 재귀 호출
  for i in graph[v]:
    # 인접 노드가 방문되지 않았다면
    if not visited[i]:
      dfs(graph, i, visited)
  
# 각 노드가 연결된 정보(2차원 리스트)
graph = [
  [],   # 노드 번호가 1번부터 시작하므로 비워두는게 좋음
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보
visited = [False] * 9

dfs(graph, 1, visited)  # DFS 호출