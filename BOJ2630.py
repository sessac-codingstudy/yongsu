#https://www.acmicpc.net/problem/2630

#재귀함수 문제. https://www.acmicpc.net/problem/1992와 유사하다.
#1992번 문제 풀고나서 최적화방법을 gemini가 알려줬는데 그게 기억나서 쉽게 풀었다.
#input은 용재형님이 rstrip까지 붙여서 한번에 써버리는게 편해보여서 바로 써먹게 되었다

import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

size = int(input())
data = [list(map(int, input().split())) for _ in range(size)]
count = [0,0]

def papers(x, y, size):
    if size == 1:
        count[data[y][x]] += 1
        return

    tester = data[y][x]
    for i in range(y,y+size):
        for j in range (x,x+size):
            if data[i][j] != tester:
                d = size//2
                papers(x, y, d)
                papers(x+d, y, d)
                papers(x, y+d, d)
                papers(x+d, y+d, d)
                return
    
    count[data[y][x]] += 1

papers(0, 0, size)
print(count[0])
print(count[1])
