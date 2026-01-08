#https://www.acmicpc.net/problem/10828

#스택이 뭔지 알아보는 문제. 사실 파이썬에선 리스트가 곧 스택이라 굳이 필요는 없어보인다.
#문제를 엄밀히 풀기 위해선 class로 스택을 구현하는게 맞겠지만 그냥 리스트를 썼다.
#input()은 더이상 사용하지 않는 것으로. 생각보다 작동 시간 차이가 많이 난다.
#반드시 sys.stdin.readline으로 사용하자.
#주의점 : readline도 끝에 \n이 붙는다. 스트립을 하던가 스플릿을 하던가 해야함. 스플릿하면 무조건 리스트되니까 [0]도 붙일 것.

import sys

input = sys.stdin.readline
actions = int(input())

def stack(data):
    order = input().strip()

    if order == "pop":
        if len(data) == 0:
            print(-1)
        else:
            print(data.pop())
    elif order == 'size':
        print(len(data))
    elif order == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])
    else:
        data.append(int(order.split()[1]))

my_list = []
for _ in range(actions):
    stack(my_list)
