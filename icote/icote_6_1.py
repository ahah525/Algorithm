n = int(input())
arr = [int(input()) for _ in range(n)]  # n개의 수

# 1. 정렬 라이브러리(내림차순)
print(*sorted(arr, reverse=True))

'''
# 2. 선택 정렬(내림차순)
for i in range(len(arr)):
  max_idx = i  # 최댓값 인덱스
  for j in range(i + 1, len(arr)):
    # 최댓값 인덱스 갱신
    if arr[max_idx] < arr[j]:  max_idx = j
  # 최솟값 & 맨 앞 값 swap
  arr[max_idx], arr[i] = arr[i], arr[max_idx]
print(*arr)
'''
'''
# 3. 삽입 정렬(내림차순)
for i in range(1, len(arr)):
  for j in range(i, 0, -1):
    # 현재값이 앞의 값보다 크면 swap
    if arr[j] > arr[j - 1]:
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
    # 현재값이 앞의 값보다 작거나 같다면 탈출
    else:  break
print(*arr)
'''
'''
# 4. 퀵 정렬
def quickSort(arr, start, end):
  # 원소 개수가 1개 이하면 종료
  if start >= end:  return

  pivot = start  # pivot은 첫번째 원소로
  left = start + 1  # 왼쪽에서부터 찾는 작은 수(pivot 다음 수부터)
  right = end    # 오른쪽에서부터 찾는 큰 수

  # 2개로 분할
  while True:
    # pivot보다 작은 수 찾기
    while left <= end and arr[left] >= arr[pivot]: 
      left += 1
    # pivot보다 큰 수 찾기
    while right >= start + 1 and arr[right] <= arr[pivot]:
      right -= 1
    print(left, right)
    # 엇갈렸다면 pivot과 right swap
    if left > right:
      arr[pivot], arr[right] = arr[right], arr[pivot]
      break
    # 엇갈리지않았다면 left와 right swap
    else:
      arr[left], arr[right] = arr[right], arr[left]
  # 분할 후 왼쪽, 오른쪽 부분에 대해 각각 내림차순 정렬
  quickSort(arr, start, right - 1)
  quickSort(arr, right + 1, end)
  
quickSort(arr, 0, len(arr) - 1)
print(*arr)
'''
'''
# 5. 계수 정렬
counting = [0] * (100001)  # 1이상 100,000이하의 자연수이므로

for i in arr:
  counting[i] += 1

for i in range(len(counting) - 1, -1, -1):
  for j in range(counting[i]):
    print(i, end=' ')
'''