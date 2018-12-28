# 11654
# 문제 :
#   알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

import sys

def beak_11654(input):
    '''
    :param input: 리스트 형식
    :return: output 벡터
    '''
    output = [ord(x) for x in input]

    return output.pop()

input = list(sys.stdin.readline().rstrip().split())

print(beak_11654(input))
