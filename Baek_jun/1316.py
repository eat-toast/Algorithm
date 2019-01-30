# 주의 사항

# 1. 단어 N개를 입력으로 받아
# 그룹단어의 정의 : 한 단어는 발생한 순간 좌우 같은 단어들과 나열되어 있어야 한다.

how_many = int(input())

result = 0
for i in range(how_many):
    s = input()  # 문자열 INPUT

    for idx, letter in enumerate(s):
        src = []
        for j in range(len(s)):
            if s.find(letter, j) > -1 :
                src.append(s.find(letter, j))

        if max(src) - min(src)+1 == s.count(letter):
            continue
        else:
            break
    if idx == len(s)-1 :
        result += 1
    else:
        continue

print(result)