#https://www.acmicpc.net/problem/9095

# 재귀 - 점화식
# 처음엔 recur(n) = recur(n-1) * a + b 로 답이 나올 줄 알았다. 그런데 아니었음.
# 결국 n=1부터 n=6까지 직접 손계산해보고 알았는데, 원래는 이렇게 하면 안된다고 함.
# 점화식 재귀 찾는법
# 1. 종료지점을 찾는다. 이 문제같은 경우 1,2,3 세 개를 쓸수 있으니 recur(1), recur(2), recur(3)은 종료지점이라고 눈치 채야함.
# 2. 그러면 다음 recur(4)는 종료지점 3개 지지고 볶으면 나오게 되어있다.

import sys

def UNDOTR(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return UNDOTR(num-1) + UNDOTR(num-2) + UNDOTR(num-3)

input = sys.stdin.readline

for _ in range(int(input())):
    print(UNDOTR(int(input())))
