#https://www.acmicpc.net/problem/2206

#BFS 최단경로 탐색 문제
#오늘은 알고리즘 개념 정리를 위해서 gemini의 도움을 받았다.

from collections import deque

def solve_maze(n, m, grid):
    # 상하좌우 이동용
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 3차원 방문 체크 배열: [행][열][벽파괴여부(0 or 1)]
    # visited[x][y][0] -> 벽 안 부수고 도달
    # visited[x][y][1] -> 벽 부수고 도달
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    # 큐: (x, y, 벽파괴여부) 
    # 거리는 visited 배열에 직접 기록하는 방식 추천 (visited값이 0이면 방문 안 함, 1이상이면 거리)
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1  # 시작점 거리 1

    while queue:
        x, y, broken = queue.popleft()

        # 목표 지점 도착?
        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                
                # CASE 1: 다음 칸이 벽이 아니고(0), 아직 방문 안 했을 때
                if grid[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    # 여기에 로직 작성: 그냥 가면 됨
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))

                # CASE 2: 다음 칸이 벽(1)인데, 아직 벽을 부순 적이 없다면(broken == 0)?
                elif grid[nx][ny] == 1 and broken == 0:
                    # 여기에 로직 작성: 벽을 부수고(상태 변경) 이동
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    
    return -1 # 도달 불가능

n, m = map(int,input().split())
grid = []
for _ in range(n):
    row = input()
    grid.append([int(row[i]) for i in range(m)])
print(solve_maze(n, m, grid))
