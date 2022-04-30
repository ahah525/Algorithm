# 1. 이진 탐색
def binary_search(array, target, start, end):
  global cnt
  while True:
    # 시작점과 끝점이 엇갈리면 종료
    if start > end:  return -1
    mid = (start + end) // 2  
    # 1. 탐색값이 중간값보다 크면 오른쪽 탐색
    if array[mid] < target:
      start = mid + 1
    # 2. 탐색값이 중간값보다 작으면 왼쪽 탐색
    elif array[mid] > target:
      end = mid - 1
    # 3. 탐색값이 중간값과 같다면 왼쪽, 오른쪽 탐색
    else:
      cnt += 1
      left, right = mid - 1, mid + 1
      # 왼쪽에서 탐색값 더 찾기
      while left >= start and array[left] == target:  
        cnt += 1
        left -= 1
      # 오른쪽에서 탐색값 더 찾기
      while right <= end and array[right] == target:  
        cnt += 1
        right += 1
      return cnt
    
n, x = map(int, input().split())  # 원소 개수, 탐색값
array = list(map(int, input().split()))  # n개의 원소
cnt = 0  # 탐색값의 개수

print(binary_search(array, x, 0, n - 1))

'''
# 1. bisect 라이브러리 이용
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 범위에 있는 개수 반환
def count_by_range(array, left_value, right_value):
  left_idx = bisect_left(array, left_value)
  right_idx = bisect_right(array, right_value)
  return right_idx - left_idx

n, x = map(int, input().split())  # 원소 개수, 탐색값
array = list(map(int, input().split()))  # n개의 원소
# x인 원소의 개수
cnt = count_by_range(array, x, x)

if cnt == 0:  print(-1)
else:  print(cnt)
'''

