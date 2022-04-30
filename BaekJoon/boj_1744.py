n = int(input()) # 수열 크기
positive = []    # 양수 리스트
negative = []    # 0 / 음수 리스트
sum = 0          # 수열의 합

# 양수, 음수 리스트 분리 입력
for _ in range(n):
  num = int(input())
  # 양수이면
  if(num > 0):
    positive.append(num)
  # 0이거나 음수이면
  else:
    negative.append(num)

positive.sort(reverse = True)  # 양수 내림차순 정렬
negative.sort()                # 음수 오름차순 정렬

# 양수 리스트 합
for i in range(0, len(positive), 2):
  # 마지막 인덱스가 아니면
  if(i != len(positive) - 1):
    # 둘 중 하나라도 1이면
    if(positive[i] == 1 or positive[i + 1] == 1):
      sum += positive[i] + positive[i + 1]  # 두 값 덧셈
    # 두 값이 모두 1이 아니면
    else:
      sum += positive[i] * positive[i + 1]  # 두 값 곱셈
  # 마지막 인덱스이면
  else:
    sum += positive[i]  # 첫번째 값만 더하기

# 음수 리스트 합
for i in range(0, len(negative), 2):
  # 마지막 인덱스가 아니면
  if(i != len(negative) - 1):
    sum += negative[i] * negative[i + 1]
  # 마지막 인덱스이면
  else:
    sum += negative[i]
    
print(sum)

'''
n = int(input())  # 수열 크기
arr = [int(input()) for _ in range(n)]  # 수열
arr.sort(reverse=True)  # 내림 차순 정렬
sum = 0
n_idx = 50  # 0/음수 시작 인덱스

for i in range(0, n, 2):
  # 수열 크기가 1이거나 마지막 인덱스이면
  if(n == 1 or i > n -2):
    sum += arr[i]
    break
  
  # 둘다 양수이면
  if(arr[i] > 0 and arr[i + 1] > 0):
    # 둘 중 하나라도 1이면
    if(arr[i] == 1 or arr[i + 1] == 1):
      sum += (arr[i] + arr[i + 1])
    # 둘 다 1이 아니면
    else:
      sum += (arr[i] * arr[i + 1])
  # 첫번째 값만 0보다 크면
  elif(arr[i] > 0 and arr[i + 1] <= 0):
    sum += arr[i]  # 첫번째 값만 더하기
    n_idx = i + 1  # 0/음수 시작 인덱스 설정
    break
  # 둘다 음수이면
  elif(arr[i] <= 0):
    n_idx = i
    break

# 0/음수가 1개라도 있으면
if(n_idx != 50):
  arr = sorted(arr[n_idx:])  # 오름차순 정렬

  # 음수 합
  for i in range(0, len(arr), 2):
    # 맨 마지막 인덱스이면
    if(i == (len(arr) - 1)):
      sum += arr[i]
    else:
      sum += arr[i] * arr[i + 1]
  
print(sum)
'''
