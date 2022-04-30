n = int(input())
temp = []

# DFS
def dfs(depth):
  # 깊이가 n이 되면 종료
  if depth == n:
    print(*temp)
    return

  for i in range(1, n + 1):
    # 아직 사용하지 않은 숫자면
    if i not in temp:
      temp.append(i)  # 사용할 숫자 넣기
      dfs(depth + 1)    # 다음 깊이로 dfs 호출
      temp.pop()      # 사용한 숫자 꺼내기
dfs(0)
'''
from itertools import permutations

n = int(input())
graph = [i for i in range(1, n + 1)]  # 1 ~ n 

for i in permutations(graph):
  print(' '.join(map(str, i)))
'''
'''
for i in permutations(graph):
  for j in i:
    print(j, end= " ")
  print()
'''