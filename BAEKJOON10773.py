#https://www.acmicpc.net/problem/10773

#stack을 활용한 쉬운 예시문제

import sys

input = sys.stdin.readline

K = int(input().strip())
nums = []

for _ in range(K):
    order = int(input().strip())
    if order == 0:
        nums.pop()
    else:
        nums.append(order)

print(sum(nums))
