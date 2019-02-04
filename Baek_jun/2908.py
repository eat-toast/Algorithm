# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

import sys

input_nums = sys.stdin.readline()
A, B = input_nums.split(' ')
A = int(A[::-1])
B = int(B[::-1])

print(max(A, B))
