#https://www.acmicpc.net/problem/5648

#이 문제는 입력이 몇 줄인지 포맷이 명확하지가 않았다.
#따라서 input을 사용하기 곤란해 sys를 활용하여 입력을 받았다.
#lines = sys.stdin.readlines() 를 이용하면 lines에는 입력을 줄바꿈 기준으로 나눠 리스트로 저장된다.
#주의점 : lines 내 원소들의 끝에 "\n" 텍스트가 붙어있다. .strip()으로 \n을 지워줘야 함.

#data.sort()는 inplace함수로 none을 반환한다는 점을 잊지말자.

import sys

lines = sys.stdin.readlines()
data = []

for line in lines:
    for num in line.strip().split():
        data.append(int(num[::-1]))

data.pop(0)
data.sort()
for i in data:
    print(i)
