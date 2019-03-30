import sys

node = list(map(int, sys.stdin.readline().rstrip().split(' ')))

if node[7]>node[6] and node[6]>node[5]and node[5]>node[4]and node[4]>node[3]and node[3]>node[2]and node[2]>node[1]and node[1]>node[0] :
    print('ascending')
elif node[7]<node[6] and node[6]<node[5]and node[5]<node[4]and node[4]<node[3]and node[3]<node[2]and node[2]<node[1]and node[1]<node[0] :
    print('descending')
else:
    print('mixed')

