# 선택 정렬(Insertion Sort)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 오름차순 정렬
# 1번 인덱스부터 시작
for i in range(1, len(array)):
  # 0 ~ i 인덱스 정렬
  for j in range(i, 0, -1):
    # 현재값이 왼쪽값보다 크면 탈출
    if array[j] > array[j - 1]:  break
    # 현재값이 왼쪽값보다 작다면 swap
    else:
      # swap (현재값 & 왼쪽값 서로 바꾸기)
      array[j], array[j - 1] = array[j - 1], array[j]

print(array)
      
      
       