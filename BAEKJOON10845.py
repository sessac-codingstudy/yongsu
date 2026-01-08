#https://www.acmicpc.net/problem/10845

#10828과 동일. collections.deque로 이미 훌륭한 큐가 구현되어 있다.
#class로 구현 가능하다. 원리는 Node라는 클래스를 만들고 data가 들어오면 해당 data의 앞data, 뒷data 정보를 함께 담은 Node클래스 형태로 변환해서 기록하는 것.

import sys
from collections import deque

input = sys.stdin.readline
actions = int(input())

def stack(data):
    order = input().strip()

    if order == "pop":
        if len(data) == 0:
            print(-1)
        else:
            print(data.popleft())
    elif order == 'size':
        print(len(data))
    elif order == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
    elif order == 'back':
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])
    else:
        data.append(int(order.split()[1]))

my_list = deque()
for _ in range(actions):
    stack(my_list)
