# 1. 집합(set) 이용
n = int(input())  # 부품 개수
array = set(map(int, input().split()))  # n개의 부품목록(집합)
m = int(input())  # 구매 원하는 부품 개수
order = list(map(int, input().split()))  # m개의 부품 위시리스트

for i in order:
  # 해당 부품이 부품목록에 있는지 검사
  if i in array:
    print("yes", end=" ")
  else:
    print("no", end=" ")

'''
# 3. 계수 정렬
n = int(input())       # 부품 개수
array = [0] * 1000001  # 부품목록 카운팅
for i in map(int, input().split()):
  array[i] = 1  # 체크
m = int(input())  # 구매 원하는 부품 개수
order = list(map(int, input().split()))  # m개의 부품 위시리스트

for i in order:
  # 부품이 있는지 확인
  if array[i] == 1:  print("yes", end=" ")
  else:  print("no", end=" ")
'''

'''
# 2. 이진 탐색
def binary_search(array, target, start, end):
  while True:
    # 시작점과 끝점이 엇갈렸으면 못찾음
    if start > end:  return "no"
    mid = (start + end) // 2  # 중간점
    
    # 1. 중간값이 타겟이면
    if array[mid] == target:  return "yes"
    # 2. 중간값보다 작으면 왼쪽 탐색
    elif array[mid] > target:  end = mid - 1
    # 3. 중간값보다 크면 오른쪽 탐색
    else:  start = mid + 1
    
n = int(input())  # 부품 개수
array = list(map(int, input().split()))  # n개의 부품목록
m = int(input())  # 구매 원하는 부품 개수
order = list(map(int, input().split()))  # m개의 부품 위시리스트

array.sort()  # 이진 탐색을 위한 오름차순 정렬

# n개의 부품에서 target
for target in order:
  print(binary_search(array, target, 0, n - 1), end=" ")
'''
