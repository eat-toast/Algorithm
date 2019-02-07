T = int( input() ) # 시행할 테스트 케이스 수
for _ in range(T):

    k = int( input() ) # k 층
    n = int( input() ) # n 호
    if n == 1 :
        print(1)
    else:

        zero = [i+1 for i , x in enumerate(range(n))] # 0층을 표현하기 위해
        temp = [0] * n # n호 만큼 빈 방을 만든다. (복도형 아파트를 생각한다)

        apt = [zero] # 아파트의 정보

        # 아파트 만들기
        for _ in range(1, k+1): # 1층부터 k층 까지
            apt.append(temp[:]) # 단순 복사가 아닌, 새로운 객체를 만들기 위해 : 로 input 한다.

        # 1호는 바로 만든다.
        person = 0

        for floor in range(1, k + 1):
            apt[floor][person] = 1

        # 사람 채워 넣기
        while(1):
            person += 1
            for floor in range(1,k+1):
                apt[floor][person] = apt[floor-1][person] + apt[floor][person-1]

            if person == n-1 :
                break

        print( apt[k][n-1] )