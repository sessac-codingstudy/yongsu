#https://www.acmicpc.net/problem/1992

#재귀 탐색문제
#내가 만든 코드는 크기가 몇이든 무조건 1x1범위까지 탐색했다가 올라오면서 서로 같으면 압축하는 방식이라서 메모리를 많이 잡아먹는다.
#그 반증으로 메모리를 신경쓰지 않은 최초 제출에선 메모리초과 처리가 되었다. 
#메모리 제한이 이보다 더 적다면 재귀 호출 전, for문을 이용해서 데이터탐색 먼저 하고 데이터가 모두 같다면 강제 리턴하는 방식으로 가는 것이 좋겠다.

import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

size = int(input())
data = [input() for _ in range(size)]

def quadtree(start_x, start_y, size, data):
    if size == 1:
        return data[start_y][start_x]
    else:
        s = quadtree(start_x, start_y, size//2, data)
        i = quadtree(start_x + size//2, start_y, size//2, data)
        z = quadtree(start_x, start_y + size//2, size//2, data)
        e = quadtree(start_x + size//2, start_y + size//2, size//2, data)
        if s==i==z==e and len(s) == 1:
            return s
        else: return f"({s}{i}{z}{e})"

print(quadtree(0,0,size, data))
