day = {6: 'SUN', 0: 'MON', 1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT'}
mon = {1 : 31, 2: 28, 3:31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# 1월 1일이 Mon 이다
# 시작일로 부터 현재까지 지난일 수를 더하고 7로 나누면 현재 요일이 나온다.

x, y = map(int, input().split(' '))

after_mon = 0
for M in range(1, x, 1):
    after_mon += mon[M]

after_day = after_mon + y
idx = after_day % 7

if idx == 0:
    print(day[6])
else:
    print(day[idx-1])