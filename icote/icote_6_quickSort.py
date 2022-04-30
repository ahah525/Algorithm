# 퀵 정렬(Quick Sort)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 오름차순 정렬
def quickSort(array, start, end):
  if start >= end:  # 원소가 1개가 되면 종료
    return
  pivot = start  # pivot은 첫 번째 원소   
  left = start + 1
  right = end
  
  while left <= right:
    # pivot보다 큰 값을 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1  # 오른쪽으로 한칸 이동
    # pivot보다 작은 값을 찾을 때까지 반복
    while right > start and array[right] >= array[pivot]:
      right -= 1  # 왼쪽으로 한칸 이동
    # 왼쪽값과 오른쪽 값이 엇갈리면
    if left > right:
      # 작은 데이터(오른쪽 값)과 pivot을 서로 변경
      array[pivot], array[right] = array[right], array[pivot]
    # 왼쪽값과 오른쪽 값이 엇갈리지 않았으면
    else:
      # 큰 데이터(왼쪽값)과 작은 데이터(오른쪽 값)을 변경
      array[left], array[right] = array[right], array[left]

  # 분할 이후 왼쪽, 오른쪽 부분에 대해 정렬 수행
  quickSort(array, start, right - 1)  # 왼쪽
  quickSort(array, right + 1, end)    # 오른쪽

quickSort(array, 0, len(array) - 1)
print(array)
'''
# 퀵 정렬(Quick Sort)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 오름차순 정렬
def quickSort(array):
  # 리스트 원소가 1개이하면 종료
  if len(array) <= 1:  
    return array
  
  pivot = array[0]  # pivot은 첫번째 원소로 설정
  tail = array[1:]  # pivot을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분(pivot보다 작거나 같은 값)
  right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분(pivot보다 큰 값)

  #print(left_side, right_side)
  # 분할 이후 왼쪽, 오른쪽 부분 각각 정렬 수행 후 전체 리스트 반환
  return quickSort(left_side) + [pivot] + quickSort(right_side)

print(quickSort(array))
'''
