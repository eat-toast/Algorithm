import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    quiz = list(sys.stdin.readline().rstrip())

    mile_stone = len(quiz) #들어온 길이에 해당하는 값을 부여

    reward = []

    for i in range(mile_stone):
        if quiz[i] == 'O':
            reward.append(1)
        else:
            reward.append(0)

        if quiz[i] == quiz[i-1] and quiz[i] == 'O' and i > 0 :
            reward[i] =  reward[i] + reward[i-1]

    print(sum(reward))