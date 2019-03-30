import sys

n = int(sys.stdin.readline().rstrip())
count = 0 #최종 예측 수

N = list(str(n)) # input 데이터를 문자로 슬라이싱

for i in range(1,n+1,1):

    if len(str(i)) <= 2: #한 자리 수라면
        count += 1 #무조건 count + 1

    else:
        diff_1 = int(str(i)[0]) - int(str(i)[1])
        diff_2 = int(str(i)[1]) - int(str(i)[2])
        if diff_1 == diff_2:
            count += 1