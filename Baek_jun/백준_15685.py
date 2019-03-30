# 드래곤 커브
# Y축 방향이 기존에 알던 방향과 반대이다.
# 하지만, 2차원 상에서 회전 변환은 동일하다.

'''
방향 (d)
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
'''
result = []


def rotation(x, y):
    new_x = -y
    new_y = x

    return (new_x, new_y)


def make_end_point(x, y, d):
    if d == 0:
        end_point = (x + 1, y)
    elif d == 1:
        end_point = (x, y - 1)
    elif d == 2:
        end_point = (x - 1, y)
    elif d == 3:
        end_point = (x, y + 1)

    return end_point


N = int(input())

for _ in range(N):
    x, y, d, g = map(int, input().split(' '))

    # 시작점을 받음
    start_point = (x,y)
    end_point = make_end_point(x,y, d)

    # 드래곤의 좌표
    dragon = [start_point, end_point]

    # g 세대만큼 반복문 돌리기
    for gen in range(g):
        end_point = dragon[-1]
        center_dragon = [(x - end_point[0], y - end_point[1]) for x, y in dragon]
        iter_center_dragon = center_dragon[:]
        iter_center_dragon.reverse()

        # 중심이동
        for cx, cy in iter_center_dragon:
            rotated = rotation(cx, cy)
            if rotated not in center_dragon:
                center_dragon.append(rotated)

        # 중심 재이동
        dragon = [(x + end_point[0], y + end_point[1]) for x, y in center_dragon]

    result += dragon

result = list(set(result))


temp_x = 0
temp_y = 0
for x , y in result:
    temp_x = max(temp_x, x)
    temp_y = max(temp_y, y)
max_x = temp_x
max_y = temp_y

# 0,0 부터 max_x, max_y까지 검사 시행.
num_sq = 0

center = (0,0)
for x in range(0, max_x+1):
    for y in range(0, max_y+1):
        criterion = (center[0] + x , center[1] + y)
        temp1 = (criterion[0], criterion[1])
        temp2 = (criterion[0] - 1, criterion[1])
        temp3 = (criterion[0] - 1, criterion[1] - 1)
        temp4 = (criterion[0], criterion[1] -1)

        if ( temp2 in result ) and ( temp3 in result ) and ( temp4 in result ) and ( temp1 in result ) :
            num_sq += 1

print(num_sq)