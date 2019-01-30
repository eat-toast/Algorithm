import sys

# input string
s = sys.stdin.readline().rstrip()

# to Upper string
S = s.upper()

# 1. 알파벳 set을 만들고, count+1씩 한다. --> 가장 높은 숫자를 추출 (동치 시 ? 출력)
alphabet = [0] * 26
for letter in S:
    alphabet[ord(letter) - 65] += 1

max_int = max(alphabet)

if alphabet.count(max_int) >= 2:
    print('?')
else:
    print(chr(alphabet.index(max_int) + 65))