import sys

score = list(map(int, sys.stdin.readline().rstrip().split('\n')))

group_score = [x for x in score if x> 40] + [40 for x in score if x< 40]
mean_score = sum(group_score) / len(group_score)
print('%d' %mean_score)
