n = int(input())  # 질문 횟수
# 세자리수, 스트라이크 개수, 볼 개수
graph = [list(map(int, input().split())) for _ in range(n)]
num = []    # 암호
answer = 0  # 가능성이 있는 답 개수

# DFS
def dfs(depth):
  if depth == 3:
    global answer
    # 모든 질문에 대해 검사
    for i in range(n):
      # 각 자리수 검사(스트라이크, 볼 개수 세기)
      strike, ball = 0, 0
      for j in range(3):
        target = str(graph[i][0])
        # j번째 자리수가 같다면 스트라이크
        if int(target[j]) == num[j]:  strike += 1
        # 자리수는 다르지만 있다면 볼
        elif int(target[j]) in num:  ball += 1
      # 스트라이크, 볼 수가 하나라도 다르다면 종료
      if strike != graph[i][1] or ball != graph[i][2]:
        return  
    #print(num)
    answer += 1  # 모든 질문에 통과하면 정답 개수 변경
    return     
  # 9개 숫자중에 하나 선택하기
  for i in range(1, 10):
    # 선택하지 않은 수라면
    if i not in num:    
      num.append(i)
      dfs(depth + 1)
      num.pop()

dfs(0)
print(answer)
'''
from itertools import permutations

n = int(input())  # 질문 횟수
# 세자리수, 스트라이크 개수, 볼 개수
graph = [list(map(int, input().split())) for _ in range(n)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 가능한 숫자
answer = 0  # 가능성이 있는 답 개수

# (1~9)에서 3개 뽑기
for num in permutations(numbers, 3):
  isAnswer = True  # 정답 여부
  # 모든 질문에 대해 검사
  for i in range(n):
    if not isAnswer:  break
    # 각 자리수 검사(스트라이크, 볼 개수 세기)
    strike, ball = 0, 0
    for j in range(3):
      target = str(graph[i][0])
      # j번째 자리수가 같다면 스트라이크
      if int(target[j]) == num[j]:  strike += 1
      # 자리수는 다르지만 있다면 볼
      elif int(target[j]) in num:  ball += 1
    # 스트라이크, 볼 수가 하나라도 다르다면 종료
    if strike != graph[i][1] or ball != graph[i][2]:
      isAnswer = False
      break 
  if isAnswer:  answer += 1  # 모든 질문에 통과하면 정답 개수 변경
print(answer)
'''

