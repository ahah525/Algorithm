# 2. 이진 탐색(반복문 구현)
def binary_search(array, target, start, end):
  while True:
    # 시작점과 끝점이 엇갈리면 종료
    if start > end:  return None
    mid = (start + end) // 2

    # 1. 타겟이 중간점과 같다면 인덱스 리턴
    if target == array[mid]:  return mid
    # 2. 타겟이 중간점보다 작다면 왼쪽 탐색
    elif target < array[mid]:
      end = mid - 1  # 끝 점을 (중간점 - 1)로 변경
    # 3. 타겟이 중간점보다 크다면 오른쪽 탐색
    else:
      start = mid + 1  # 끝 점을 (중간점 + 1)로 변경
    
n, target = map(int, input().split())  # 원소 개수, 찾고자하는 값
array = list(map(int, input().split()))  # n개의 원소

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result + 1)

'''
# 1. 이진 탐색(재귀 구현)
def binary_search(array, target, start, end):
  # 시작점과 끝점이 엇갈리면 종료
  if start > end:  return None
  mid = (start + end) // 2  # 소수점은 버림

  # 1. 타겟이 중간점과 같다면 인덱스 리턴
  if target == array[mid]:  return mid
  # 2. 타겟이 중간점보다 작다면
  elif target < array[mid]:
    # mid 왼쪽 부분에 대해 이진 탐색 수행
    return binary_search(array, target, start, mid - 1)
  # 3. 타겟이 중간점보다 크다면
  else:
    # mid 오른쪽 부분에 대해 이진 탐색 수행
    return binary_search(array, target, mid + 1, end)

n, target = map(int, input().split())  # 원소 개수, 찾고자하는 값
array = list(map(int, input().split()))  # n개의 원소

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result + 1)
'''