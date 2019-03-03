T = int( input() ) # 입력 횟수

prize_1 = {500: 1, 300: 2, 200: 3, 50: 4, 30: 5, 10: 6} # 1회 상금 정보
prize_2 = {512: 1, 256: 2, 128: 4, 64: 8, 32: 16} # 2회 상금 정보

take_prize_1 = []
winner_1 = list(prize_1.values())
for idx, x in enumerate(prize_1):
    take_prize_1.append( [x] *  winner_1[idx])

take_prize_1 = [x2 for x1 in take_prize_1 for x2 in x1]


take_prize_2 = []

winner_2 = list(prize_2.values())
for idx, x in enumerate(prize_2):
    take_prize_2.append( [x] * winner_2[idx])

take_prize_2 = [x2 for x1 in take_prize_2 for x2 in x1]

# 제이지는 과명 이번에 몇등을 했을 까?
for t in range(T):
    a, b = map(int, input().split(' ') )
    A, B = 0, 0
    if a == 0 :
        A = 0
    else:
        if a >= len(take_prize_1) + 1:
            A = 0
        else:
            A = take_prize_1[a-1]
    if b == 0:
        B = 0
    else:

        if b >= len(take_prize_2) + 1:
            B = 0
        else:
            B = take_prize_2[b-1]

    print((A + B) * 10000)