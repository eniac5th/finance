# 첫번째 상한가 이후에 하락하여 다음 고점 가격 위치 구하는 프로그램
# 아래 URL를 참조해서 만들어보았다.
# https://www.youtube.com/watch?v=HKtwFOwKOdw&t=800s

# 화신테크 (5/16~5/18일까지 1차 상승후 2차(6/28) 고점값 구하는 것를 에로 한다.
#firstLowCost = 1975
#firstHighCost = 4090
#furtureIncrease(다음고점 가격 위치) --> 5147.5

firstLowCost = int(input('firstLowCost(처음 저점 가격 입력) '))
firstHighCost = int(input('firstHighCost(처음 고점 가격 입력) '))


increase = (firstHighCost - firstLowCost) / firstLowCost * 100

print('증가율:', increase)
if increase > 100 : # 상승률이 100% 넘어야 의미가 있다.
    furtureIncrease  = (increase * 1.5) * (firstLowCost / 100) + firstLowCost
    print('미래고점: ', furtureIncrease)
else:
    print('증가율이 100를 넘어야 한다')




