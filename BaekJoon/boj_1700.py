n, k = map(int, input().split())  # 구멍개수, 총 사용횟수
order = list(map(int, input().split()))  # 사용 순서
multitap = [0] * n  # 구멍 개수만큼 초기화
cnt = 0    # 픓러그 빼는 횟수
 
for i in range(k):
  pivot = order[i]  # 꽂아야 할 현재 플러그
  
  # 1. 멀티탭에 현재 플러그가 있는 경우
  if(pivot in multitap):
    continue
  # 2. 멀티탭에 빈 구멍이 있을 경우
  elif(0 in multitap):
    multitap[multitap.index(0)] = pivot
  # 3. 멀티탭에 현재 플러그가 없는 경우
  else:
    max_idx = 0   # 멀티탭 플러그 중 가장 늦게 사용되는 순서 인덱스
    plug_idx = 0   # 멀티탭에 꽂을 위치 인덱스 
    
    # 멀티탭 플러그들에 대해 
    for j in range(n):
      # 멀티탭 플러그가 더이상 사용되지 않으면
      if(multitap[j] not in order[i:]):
        plug_idx = j  # 뺄 플러그 지정 후 탈출
        break
      # 멀티탭 플러그에서 가장 늦게 사용되는 플러그 인덱스 구하기
      elif(max_idx < order[i:].index(multitap[j])):
        max_idx = order[i:].index(multitap[j])  # 사용 순서 인덱스
        plug_idx = j  # 멀티탭 인덱스
    # plug-in, plug-out     
    multitap[plug_idx] = pivot
    cnt += 1  # 뺀 횟수 증가
print(cnt)