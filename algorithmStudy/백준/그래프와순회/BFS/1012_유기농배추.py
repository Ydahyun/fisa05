from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]   # x(열)
dy = [0,0,1,-1]   # y(행)

def bfs(y, x):  # (행, 열)
    q = deque()
    q.append((y, x))
    graph[y][x] = 0  # 방문 처리

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())   # M=가로(열), N=세로(행)
    graph = [[0]*M for _ in range(N)]     # N x M

    for _ in range(K):
        x, y = map(int, input().split())  # (열, 행)
        graph[y][x] = 1

    cnt = 0
    for i in range(N):        # 행
        for j in range(M):    # 열
            if graph[i][j] == 1:
                bfs(i, j)     # (행, 열)
                cnt += 1
    print(cnt)
