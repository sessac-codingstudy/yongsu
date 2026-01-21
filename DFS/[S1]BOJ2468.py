#https://www.acmicpc.net/problem/2468

# dfs탐색문제

import sys
sys.setrecursionlimit(10**6)

def safe_islands():
    size = int(input())
    grid = [list(map(int,input().split())) for _ in range(size)]
    max_height = 0
    min_height = 100
    max_islands = 1

    for rows in grid:
        if max(rows) > max_height:
            max_height = max(rows)
        if min(rows) < min_height:
            min_height = min(rows)
    
    def dfs(r, c, h):
        if (r < 0 or r >= size or c < 0 or c >= size or
            (r, c) in visited or grid[r][c] <= h):
            return

        visited.add((r, c))

        dfs(r - 1, c, h)
        dfs(r + 1, c, h)
        dfs(r, c - 1, h)
        dfs(r, c + 1, h)

    for water_height in range(min_height,max_height):
        visited = set()
        islands = 0
        for r in range(size):
            for c in range(size):
                if grid[r][c] > water_height and (r, c) not in visited:
                    islands += 1
                    dfs(r, c, water_height)
        if islands > max_islands:
            max_islands = islands
    
    return max_islands

print(safe_islands())
