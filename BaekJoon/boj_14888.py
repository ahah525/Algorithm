from itertools import permutations
import sys
input = sys.stdin.readline

min_res = 1e9
max_res = -1e9
n = int(input())
num = list(map(int, input().split()))  # n개 정수
# 덧셈, 뺄셈, 곱셈, 나눗셈 개수
cnt = list(map(int, input().split()))
operator = []

for i in range(4):
  for j in range(cnt[i]):
    operator.append(i)

for o in permutations(operator):
  res = num[0]  # 첫번째 값으로 초기화
  for j in range(n - 1):
    # 덧셈이면
    if o[j] == 0:  res += num[j + 1]
    elif o[j] == 1:  res -= num[j + 1]
    elif o[j] == 2: res *= num[j + 1]
    elif o[j] == 3:
      # 둘 다 양수이면 몫을 계산
      res = int(res / num[j + 1])
      #if(res > 0 and num[j + 1] > 0):  res //= num[j + 1]
      #elif(res < 0):  res = -(-res // num[j + 1])
  if res > max_res:  max_res = res
  if res < min_res:  min_res = res
print(max_res, min_res, sep="\n")

'''
import sys
input = sys.stdin.readline

# DFS
def dfs(depth, res):
  global min_res, max_res
  if depth == n - 1:
    max_res = max(max_res, res)
    min_res = min(min_res, res)
    return

  for i in range(len(operator)):
    # 선택하지 않은 연산자라면
    if not check[i]:
      # 덧셈
      if operator[i] == 0:
        check[i] = True     
        dfs(depth + 1, res + num[depth + 1])
        check[i] = False
      # 뺄셈
      elif operator[i] == 1:
        check[i] = True   
        dfs(depth + 1, res - num[depth + 1])
        check[i] = False
      # 곱셈
      elif operator[i] == 2:  
        check[i] = True   
        dfs(depth + 1, res * num[depth + 1]) 
        check[i] = False
      # 나눗셈
      elif operator[i] == 3:
        check[i] = True   
        dfs(depth + 1, int(res / num[depth + 1]))
        check[i] = False
      
min_res = 1e9  
max_res = -1e9
n = int(input())
num = list(map(int, input().split()))  # n개 정수
# 덧셈, 뺄셈, 곱셈, 나눗셈 개수
cnt = list(map(int, input().split()))
operator = []
check = [False] * (n - 1)  # 선택 여부

for i in range(4):
  for j in range(cnt[i]):
    operator.append(i)

dfs(0, num[0])    
print(max_res, min_res, sep="\n")
'''

    
  

