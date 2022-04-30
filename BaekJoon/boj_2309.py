arr = [(int(input())) for _ in range(9)]
res = sorted(arr)   # 7난장이
find = False  # 찾음 여부
total = sum(arr)  # 9난장이 합

for i in range(8):
  # 찾으면 종료
  if find:  break
  for j in range(i + 1, 9):
    # 2난쟁이를 뺀 7난쟁이의 합이 100이면
    if total - arr[i] - arr[j] == 100:
      # 2난쟁이 제거
      res.remove(arr[i])
      res.remove(arr[j])
      find = True
      break
      
for i in res:
  print(i)

'''
# 9 난쟁이의 키
arr = [(int(input())) for _ in range(9)]
arr.sort()  # 오름차순 정렬
temp = []   # 7 난쟁이 목록
find = False  # 찾음 여부

# DFS
def dfs(depth):
  global find
  # 답을 찾았으면 바로 종료
  if find: return
  # 7 난쟁이를 다 선택했다면
  if(depth == 7):
    # 키의 합이 100이면
    if sum(temp) == 100:
      for i in temp:
        print(i)
      find = True    # 찾음으로 변경
    return
  # 7 난쟁이를 다 선택하지 않았다면
  else:
    # depth 이후 값의 범위에서 선택
    for i in range(depth, len(arr)):
      # 선택하지 않았던 수라면
      if arr[i] not in temp:
        temp.append(arr[i])
        dfs(depth + 1)
        temp.pop()

dfs(0)
'''