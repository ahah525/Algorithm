# 이진 탐색
def binary_search(array, target, start, end):
  global max_length
  while True:
    # 시작점과 끝점이 엇갈리면 종료
    if start > end:  break
    mid = (start + end) // 2  # 절단기 높이
    length = 0    # 잘린 떡의 길이 총합
    # 잘린 떡의 길이 총합 계산하기
    for i in range(n):
      # 떡 높이가 절단기 높이보다 크다면
      if array[i] > mid:  length += array[i] - mid  
    
    # 1. 잘린 떡의 길이가 필요한 떡 길이보다 작다면
    if length < m:  
      end = mid - 1  # 절단기 높이 감소
    # 2. 잘린 떡의 길이가 필요한 떡 길이보다 크거나 같다면
    else:  
      start = mid + 1  # 절단기 높이 증가
      max_length = mid # 최댓값 갱신
      #print(max_length)  

n, m = map(int, input().split())  # 떡 개수, 떡 길이
array = list(map(int, input().split()))  # n개의 떡의 높이
max_length = 0  # 절단기 높이 최댓값
binary_search(array, m, 0, max(array))
print(max_length)
