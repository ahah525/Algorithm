L, C = map(int, input().split())  # 암호 길이, 알파벳목록 길이
graph = list(input().split())  # C개의 문자
graph.sort()  # 오름차순 정렬
password = []  # 가능한 암호

# DFS (암호 길이, 탐색 시작 인덱스)
def dfs(depth, idx):
  # 암호 길이가 L이 되면
  if depth == L:
    v, c = 0, 0  # 모음, 자음 개수
    # 모음, 자음 개수 구하기
    for a in password:
      if a in "aeiou":  v += 1
      else:  c += 1
    # 모음 1개, 자음 2개 이상이면
    if v >= 1 and c >= 2:
      print("".join(password))
    return
  # 암호 길이가 L이 아니면 
  # 탐색 가능한 인덱스부터 알파벳 선택하기
  for i in range(idx, C):
    a = graph[i]  # 선택한 알파벳
    # 선택하지 않은 알파벳이면
    if a not in password:
      password.append(a)
      dfs(depth + 1, i + 1)
      password.pop()
      
dfs(0, 0)

'''
from itertools import combinations

L, C = map(int, input().split())  # 암호 길이, 알파벳목록 길이
graph = list(input().split())  # C개의 문자
graph.sort()  # 오름차순 정렬

# C개의 문자에서 L개 선택(조합)
for p in combinations(graph, L):
  v, c = 0, 0  # 모음, 자음 개수
  # 모음, 자음 개수 구하기
  for a in p:
    if a in "aeiou":  v += 1
    else:  c += 1
  # 모음 1개, 자음 2개 이상이면
  if v >= 1 and c >= 2:
    print("".join(p))

'''
'''
L, C = map(int, input().split())  # 암호 길이, 알파벳목록 길이
graph = list(input().split())  # C개의 문자
graph.sort()  # 오름차순 정렬
password = []  # 가능한 암호

# DFS (암호 길이, 탐색 시작 인덱스, 모음 개수, 자음 개수)
def dfs(depth, idx, v, c):
  # 암호 길이가 L이 되면
  if depth == L:
    # 모음 1개이상, 자음 2개이상이면
    if v >= 1 and c >= 2:
      print(''.join(password))
    return
  # 암호 길이가 L이 아니면 
  # 탐색 가능한 인덱스부터 알파벳 선택하기
  for i in range(idx, C):
    a = graph[i]  # 선택한 알파벳
    # 선택하지 않은 알파벳이면
    if a not in password:
      # 모음이면
      if a in 'aeiou':
        password.append(a)
        dfs(depth + 1, i + 1, v + 1, c)  # 모음 개수 1개 증가
        password.pop()
      # 자음이면
      else:
        password.append(a)
        dfs(depth + 1, i + 1, v, c + 1)  # 자음 개수 1개 증가
        password.pop()
      
dfs(0, 0, 0, 0)
'''