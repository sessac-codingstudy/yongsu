#https://www.acmicpc.net/problem/4949

#stack을 활용한 간단한 예시문제
#오른쪽 개행문자만 지우고 싶을 때는 .rstrip() - readline에서 유용하다. 단, 오른쪽의 "공백"도 중요한 정보를 담을 때는 .rstrip('\n')로 명확히 줄바꿈만 제거하라고 명시해야한다.

import sys

while True:
    sen = sys.stdin.readline()
    chrtester = []
    sentester = 1
    if sen == '.':
        break
    for chr in sen:
        if chr in "([":
            chrtester.append(chr)
        elif chr == ")":
            if len(chrtester) == 0:
                sentester = 0
                break
            elif chrtester.pop() != "(":
                sentester = 0
                break
        elif chr == "]":
            if len(chrtester) == 0:
                sentester = 0
                break
            elif chrtester.pop() != "[":
                sentester = 0
                break
    if sentester == 1 and not chrtester:
        print('yes')
    else:
        print('no')
