#https://www.acmicpc.net/problem/11003

#단조 큐

from collections import deque
import sys

input = sys.stdin.readline

N, L = map(int,input().split())
nums = list(map(int,input().split()))
finder = deque()
result = []

for i in range(N):
    while finder and nums[finder[-1]] >= nums[i]:
        finder.pop()
    if finder and finder[0] < i - L + 1:
        finder.popleft()
    finder.append(i)
    result.append(nums[finder[0]])

print(" ".join(map(str,result)))
