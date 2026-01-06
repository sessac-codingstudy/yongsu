#https://www.acmicpc.net/problem/5648

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
