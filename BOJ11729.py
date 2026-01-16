#https://www.acmicpc.net/problem/11729

#재귀함수문제
#하노이탑에 대해 잘 이해하고있어서 쉬웠다.

import sys
sys.setrecursionlimit(10**6)

N = int(input())
K = [0]
movement = []

def hanoi(start, end, height):
    if height == 1:
        K[0] += 1
        movement.append((start, end))
        return
    
    temptower = 6 - start - end
    hanoi(start, temptower, height-1)
    K[0] += 1
    movement.append((start, end))
    hanoi(temptower, end, height-1)

hanoi(1,3,N)
print(K[0])
for i, x in enumerate(movement):
    print(x[0], end=" ")
    print(x[1])
