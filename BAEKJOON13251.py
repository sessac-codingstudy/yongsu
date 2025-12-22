# https://www.acmicpc.net/status?user_id=aighost1&problem_id=13251&from_mine=1

# combination을 사용해야 풀 수 있는 문제이다.
# combination은 nCr = n! / r! * (n-r)! 인데, 이건 까먹을 확률이 높다.
# import math 후 math.comb(n,r) 하면 메모리를 엄청 적게먹고 계산해준다.

# 배운 점 하나더. 파이썬 기본함수 sum()은 iterable이 아니고 list만 넣을 수 있다.

import math

def cobblestone():
    colors = int(input())
    numbers = list(map(int, input().split()))
    pick = int(input())
    combs = 0

    for x in numbers:
        if x >= pick:
            combs += math.comb(x, pick)
    
    total = math.comb(sum(numbers), pick)

    print(combs/total)

cobblestone()
