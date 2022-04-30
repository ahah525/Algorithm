# 선택 정렬(Selection Sort)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 오름차순 정렬
# 리스트 길이만큼 반복
for i in range(len(array)):
  min_idx = i      # 최솟값 인덱스
  for j in range(i + 1, len(array)):
    if array[min_idx] > array[j]:
      min_idx = j  # 최솟값 인덱스 갱신
  # swap(최솟값과 첫값 위치 변경)
  array[i], array[min_idx] = array[min_idx], array[i]

print(array)  