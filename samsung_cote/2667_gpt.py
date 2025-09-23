from collections import deque
import sys

input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    # 시작점이 집이 아니거나 이미 방문이면 단지 크기 0
    if graph[sx][sy] == 0 or visited[sx][sy]:
        return 0

    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1  # 시작 집 포함

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

sizes = []
for i in range(N):
    for j in range(N):
        size = bfs(i, j)
        if size > 0:
            sizes.append(size)

sizes.sort()
print(len(sizes))
for s in sizes:
    print(s)
