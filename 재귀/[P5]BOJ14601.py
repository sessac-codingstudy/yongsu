#https://www.acmicpc.net/problem/14601

# 순수 재귀함수 문제
# 논리확립에 어려움을 겪었음. 초기코드는 종료조건을 size==2로두고 일단 맨 깊은 곳 까지 내려가서 4칸 다칠하고 ㄱ자로 덧씌우는 방식이었는데,
# 임의로 테스팅좀 하다보니 반례를 직접 찾아버림 도저히 논리의 허점을 찾기가 어려워서 방식을 바꿔서 해결
# 100%확실하게 칠해야 하는 칸부터 칠하자는 방식이 잘 작용했음.

import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()

K = 2 ** int(input())
holex, holey = map(int, input().split())
holex -= 1
holey = K - holey
count = [1]
frame = [[0 for _ in range(K)] for _ in range(K)]

def tile(startx, starty, holex, holey, size):
    if size == 1:
        return
    
    half = size//2
    cenx = startx + half
    ceny = starty + half

    if holex < cenx:
        if holey < ceny:
            holequarter = 2
        else:
            holequarter = 3
    else:
        if holey < ceny:
            holequarter = 1
        else:
            holequarter = 4

    if holequarter == 2:
        frame[ceny][cenx-1] = count[0]
        frame[ceny-1][cenx] = count[0]
        frame[ceny][cenx] = count[0]
        count[0] += 1
        tile(startx, starty, holex, holey, half)
        tile(startx, ceny, cenx-1, ceny, half)
        tile(cenx, starty, cenx, ceny-1, half)
        tile(cenx, ceny, cenx, ceny, half)
    elif holequarter == 3:
        frame[ceny-1][cenx-1] = count[0]
        frame[ceny-1][cenx] = count[0]
        frame[ceny][cenx] = count[0]
        count[0] += 1
        tile(startx, starty, cenx-1, ceny-1, half)
        tile(startx, ceny, holex, holey, half)
        tile(cenx, starty, cenx, ceny-1, half)
        tile(cenx, ceny, cenx, ceny, half)
    elif holequarter == 1:
        frame[ceny-1][cenx-1] = count[0]
        frame[ceny][cenx-1] = count[0]
        frame[ceny][cenx] = count[0]
        count[0] += 1
        tile(startx, starty, cenx-1, ceny-1, half)
        tile(startx, ceny, cenx-1, ceny, half)
        tile(cenx, starty, holex, holey, half)
        tile(cenx, ceny, cenx, ceny, half)
    elif holequarter == 4:
        frame[ceny-1][cenx-1] = count[0]
        frame[ceny][cenx-1] = count[0]
        frame[ceny-1][cenx] = count[0]
        count[0] += 1
        tile(startx, starty, cenx-1, ceny-1, half)
        tile(startx, ceny, cenx-1, ceny, half)
        tile(cenx, starty, cenx, ceny-1, half)
        tile(cenx, ceny, holex, holey, half)

tile(0, 0, holex, holey, K)
frame[holey][holex] = -1

for i in range(K):
    for j in range(K):
        print(frame[i][j], end=" ")
    print("")
