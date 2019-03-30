# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
N, M = map(int, input().split(' '))

matrix = []
for _ in range(N):
    temp = list( input().split(' ') )
    matrix.append(temp)

# 치킨 & 집의 좌표를 구한뒤, 거리를 구한다.
# 모든 거리를 구한 뒤, 가까운 치킨집은 살아남는다.
# 어떤 치킨집이 가까운지는 구하지 않아도 된다.

Chiken , House = [], []

for i in range(N):
    for j in range(N):
        v = matrix[i][j]
        if v == '1':
            House.append((i,j))
        elif v == '2':
            Chiken.append((i,j))

# combinations 를 이용해 치킨집과 집사이 거리를 구한다.
from itertools import combinations

result = 1e9
for k in combinations(Chiken, M):
    s = 0
    for hx, hy in House:
        d = 1e9
        for cx, cy in k:
            d = min(d, abs(cx - hx) + abs(cy - hy))
        s += d

    result = min(result, s)

print(result)
