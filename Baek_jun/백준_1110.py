import sys
N = int(sys.stdin.readline().rstrip())

#26을 예로들면,
# 가장 오른쪽 자릿 수 6
# 2+6 = 8
#--> 68

if N < 10:
    new_N = '0'+str(N)
else:
    new_N = str(N)

step = 0
while(True):

    left_num = int(new_N [1])
    right_num = int(new_N [0]) + int(new_N [1])

    if right_num < 10:
        right_num = '0' + str(right_num)
        right_num = str(right_num)[1]
    else:
        right_num = str(right_num)[1]

    new_N = str(left_num)+str(right_num)
    step += 1
    
    if N == int(new_N):
        break


print(step)