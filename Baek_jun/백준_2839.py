import sys


total_sugar =int(sys.stdin.readline().rstrip())

## 상근이는 설탕을 3 ~ 5,000kg 배달한다. (대단한 놈)

#5kg 바구니에 모두 담아보고, 나머지가 발생하면 3kg에 담는 방식으로 진행
#만약, 모든 5kg을 사용했음에도 나눠지지 않는다면, -1 출력

step = 0
while(True):

    bag_five = total_sugar//5 - step

    #이후 남은 설탕들을 3kg 가방에 분배
    redundancy_sugar = total_sugar - bag_five*5

    bag_three = redundancy_sugar//3

    #이후 남은 설탕들을 3kg 가방에 분배
    redundancy_sugar = redundancy_sugar - bag_three*3

    if bag_five <= 0 and redundancy_sugar > 0:
        print(-1)
        break

    if redundancy_sugar == 0:
        print(bag_five + bag_three)
        break

    step += 1
