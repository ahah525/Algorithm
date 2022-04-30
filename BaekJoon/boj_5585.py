pay = int(input()) # 지불 금액
money = [500, 100, 50, 10, 5, 1]
charge = 1000 - pay  # 잔돈
res = 0  # 잔돈 개수

for m in money:
  # 탈출 조건
  if(charge == 0):
    break
  # 해당 단위로 나눠지면
  if((charge // m) != 0):
    res += charge // m  # 잔돈 개수 추가
    charge %= m    # 잔액 변경
    
print(res)
