import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

ABC = A*B*C

ABC = list(str(ABC))


zero_2_nine = {}

for i in range(10):
    zero_2_nine[i] = ABC.count(str(i)) # i번째 숫자의 갯수



zero_2_nine = list(zero_2_nine.values())

for i in range(10):
    print(zero_2_nine[i])